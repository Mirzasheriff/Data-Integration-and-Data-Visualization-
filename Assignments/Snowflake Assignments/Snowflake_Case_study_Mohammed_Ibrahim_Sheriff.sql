/* ============================================================
   01. DATABASE AND SCHEMA SETUP
============================================================ */
create database sales_db;

create or replace schema raw_schema;
create schema clean_schema;
create schema star_schema;

/* ============================================================
   02. FILE FORMAT AND STAGING SETUP
============================================================ */
create or replace file format csv_format
    type = 'csv'
    field_delimiter = ','
    skip_header = 1
    field_optionally_enclosed_by = '"'
    null_if = ('', 'null');

create stage sales_db.raw_schema.sales_stage;

/* ============================================================
   03. RAW TABLE CREATION AND INGESTION
============================================================ */
create or replace table sales_raw (
    transaction_id string,
    region string,
    country string,
    product string,
    customer string,
    sales_rep string,
    transaction_date varchar(400),
    timestamp varchar(400),
    quantity varchar(400),
    unit_price varchar(400),
    total_amount varchar(400),
    order_status string,
    payment_method string,
    product_details varchar(400),
    customer_info varchar(400)
);

copy into sales_db.raw_schema.sales_raw
from @sales_db.raw_schema.sales_stage
files = ('sales_data_dirty.csv')
file_format = csv_format
on_error = 'continue';

/* ============================================================
   04. RAW DATA CLEANING AND TYPE CASTING
============================================================ */
create or replace table raw_schema.sales_raw_refined as
select
    transaction_id,
    region,
    country,
    product,
    customer,
    sales_rep,
    try_to_date(transaction_date, 'dd-mm-yyyy') as transaction_date,
    timestamp,
    try_cast(quantity as integer) as quantity,
    try_cast(unit_price as float) as unit_price,
    try_cast(total_amount as float) as total_amount,
    order_status,
    payment_method,
    try_parse_json(product_details) as product_details,
    try_parse_json(customer_info) as customer_info
from raw_schema.sales_raw
where coalesce(transaction_id, region, country, product, customer, sales_rep, transaction_date, order_status, payment_method, quantity, unit_price, total_amount) is not null;

/* ============================================================
   05. DATA QUALITY CHECKS
============================================================ */
-- Total vs distinct transactions
select count(*) as total_transactions, count(distinct transaction_id) as distinct_transactions
from sales_raw_refined;

-- Null value check
select count(*) as null_values_count
from sales_raw_refined
where transaction_id is null or unit_price is null;

-- Negative value check
select count(*) as negative_values_count
from sales_raw_refined
where total_amount < 0;

/* ============================================================
   06. FLATTENING NESTED JSON FIELDS
============================================================ */
create or replace table clean_schema.sales_flattened as
select
    transaction_id,
    product_details:brand as brand,
    product_details:category as product_category,
    product_details:ratings as product_rating,
    product_details:specs as product_specs,
    product_details:subcategory as product_subcategory,
    customer_info:demographics as demographics,
    customer_info:preferences as preferences,
    customer_info:segment as segment
from raw_schema.sales_raw_refined;

/* ============================================================
   07. FINAL CLEANED TABLE WITH STRICT NULL FILTERING
============================================================ */
create or replace table clean_schema.sales_raw_cleaned as
select *
from raw_schema.sales_raw_refined;

delete from clean_schema.sales_raw_cleaned
where coalesce(transaction_id, region, country, product, customer, sales_rep, transaction_date, order_status, payment_method, quantity, unit_price, total_amount) is null;

/* ============================================================
   08. ENRICHMENT: PROFIT MARGIN AND SALES QUARTER
============================================================ */
alter table sales_db.clean_schema.sales_raw_cleaned add column profit_margin number;
alter table sales_db.clean_schema.sales_raw_cleaned add column sales_quarter varchar;

update sales_db.clean_schema.sales_raw_cleaned
set
    profit_margin = total_amount * 0.2,
    sales_quarter = case
        when month(transaction_date) in (1, 2, 3) then 'q1'
        when month(transaction_date) in (4, 5, 6) then 'q2'
        when month(transaction_date) in (7, 8, 9) then 'q3'
        else 'q4'
    end;

/* ============================================================
   09. STAR SCHEMA MODELING
============================================================ */
create or replace table sales_db.star_schema.dim_region as
select distinct region, country from clean_schema.sales_raw_cleaned;

create or replace table sales_db.star_schema.dim_product as
select distinct product, quantity, unit_price from clean_schema.sales_raw_cleaned;

create or replace table sales_db.star_schema.dim_customer as
select distinct customer, customer_info, region, country, order_status from clean_schema.sales_raw_cleaned;

create or replace table sales_db.star_schema.fact_sales as
select
    transaction_id,
    transaction_date,
    region,
    country,
    product_details,
    customer_info,
    sales_rep,
    quantity,
    unit_price,
    total_amount,
    profit_margin,
    sales_quarter,
    order_status,
    payment_method
from clean_schema.sales_raw_cleaned;

/* ============================================================
   10. ANALYTICS AND INSIGHTS
============================================================ */
-- Top region by sales
select region, country, sum(total_amount) as total_sales
from star_schema.fact_sales
group by region, country
order by total_sales desc
limit 1;

-- Customer segment performance
select
    split_part(customer_info, ':', 2) as customer_segment,
    sum(total_amount) as total_sales
from star_schema.fact_sales
group by customer_segment
order by total_sales desc;

-- Product brand performance
select
    split_part(product_details, ':', 2) as product_brand,
    sum(total_amount) as total_sales
from star_schema.fact_sales
group by product_brand
order by total_sales desc;

-- Order status distribution
select
    order_status,
    count(*) as order_count
from star_schema.fact_sales
group by order_status
order by order_count desc;

/* ============================================================
   11. RATING TO SALES RATIO ANALYSIS
============================================================ */
select
    product_details:brand::string as product_brand,
    regexp_substr(product_details:ratings::string, '[0-9]+(\.[0-9]+)?') as extracted_ratings,
    total_amount
from star_schema.fact_sales
limit 10;

select
    product_details:brand::string as product_brand,
    avg(cast(regexp_substr(product_details:ratings::string, '[0-9]+(\.[0-9]+)?') as float) / total_amount) as rating_to_sales_ratio
from star_schema.fact_sales
where regexp_substr(product_details:ratings::string, '[0-9]+(\.[0-9]+)?') is not null
group by product_brand
order by rating_to_sales_ratio desc;
