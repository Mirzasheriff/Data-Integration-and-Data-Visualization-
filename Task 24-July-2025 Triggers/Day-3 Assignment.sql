--=============Assignment day 03=================--

/*
Create a trigger that logs any 
update to the list_price of a product in the production.products table.
in a new table price_change_log
logid
    product_id 
    old_price
    new_price   
  change_date
*/

create table price_change_log(
logid int primary key identity(1,1),
product_id int,
old_price decimal(10,2),
new_price decimal(10,2),
change_date datetime default getdate()
)

select top 5 * from production.products

select * from price_change_log

create trigger tr_log
on production.products
after update
as
begin
   declare @Id int
   declare @oldprice int,@newprice int
   select * into #TempTable from inserted

   while (exists(select product_id from #TempTable))
   begin
   select top 1 @Id = product_id,@newprice = list_price from #TempTable
   select @oldprice = list_price from deleted where product_id=@Id
   if(@newprice <> @oldprice)
   begin
       insert into price_change_log(product_id,old_price,new_price,change_date)
       values (@Id,@oldprice,@newprice,getdate())
    end

    delete from #TempTable where product_id = @Id

    end
end


update production.products set list_price = 379.99 where product_id = 1



/*
2. Create a trigger that 
Prevent deletion of a product if it exists in any open order
*/


create trigger tr_prevent_deletion
on production.products
instead of delete
as
begin
print 'deletion is restricted'
rollback
end


create trigger tr_prevent_deletion
on production.products
instead of delete
as
begin
if exists(select 1 from deleted d join sales.order_items oi on d.product_id=oi.product_id 
join sales.orders o on oi.order_id=o.order_id where o.order_status='open')
begin
print 'deletion is restricted'
rollback
end
end



--===Assignments===--

/*
1) Total Sales by Store (Only High-Performing Stores)
List each store's name and the total sales amount (sum of quantity × list price) 
for all orders. Only include stores where the total sales amount exceeds $50,000.*/

select ss.store_name,sum(oi.quantity*oi.list_price) as total_sales_amount from sales.order_items oi
join sales.orders so on so.order_id = oi.order_id
join sales.stores ss on ss.store_id = so.store_id
group by ss.store_name
having sum(oi.quantity*oi.list_price) > 50000


/*2) Top Selling Products by Quantity 
Find the top 5 best-selling products by total quantity ordered.*/


select top 5 p.product_name,sum(oi.quantity) as total_quantity_sold from sales.order_items oi
join production.products p on p.product_id = oi.product_id group by p.product_name 
order by total_quantity_sold desc


/*3) how monthly sales totals (sum of line total) for the year 2016.*/

select month(o.order_date) as order_month,sum(oi.quantity * oi.list_price) as total_month_sales
from sales.order_items oi 
join sales.orders o on o.order_id = oi.order_id
where year(o.order_date) = 2016
group by month(o.order_date)
order by order_month



/*4) High Revenue Stores
List all stores whose total revenue is greater than ₹100,000
*/

select ss.store_name,sum(oi.quantity * oi.list_price) as total_revenue from sales.stores ss
join sales.orders o on o.store_id = ss.store_id
join sales.order_items oi on oi.order_id = o.order_id
group by ss.store_name
having sum(oi.quantity * oi.list_price) >100000
