use bikestores

create view Product_Catalog 
as
select pp.product_id,pp.product_name,pb.brand_name,pc.category_name,pp.list_price
from production.products pp join production.brands pb on pp.brand_id = pb.brand_id
join production.categories pc on pc.category_id=pp.category_id
where pp.model_year > 2018 

select * from Product_Catalog order by category_name,brand_name


alter view vw_nosales
as
select pp.product_id,pp.product_name,pp.list_price from production.products pp
where pp.product_id not in(select distinct product_id from sales.order_items)


select * from vw_nosales order by list_price desc



/*
Ranks products within each category by list price (highest first)
 
Returns only the first product per category
 
Expected Output:

category_name, product_name, list_price — only one row per category


*/


alter view ranking_data
as
select pc.category_name, pp.product_name,pp.list_price,ROW_NUMBER() over (partition by category_name order by category_name) as ranks
from production.products pp join production.categories pc on pp.category_id = pc.category_id


select * from ranking_data where ranks = 1
