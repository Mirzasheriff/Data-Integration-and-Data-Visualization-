--==Assignment==============day 2-

/*
question 1
Write a scalar-valued function that 
takes a product_id as input and 
returns the list_price of that product.
*/

alter function question1(@product_id int)
returns decimal(10,2)
as
begin
return (select list_price from production.products where product_id = @product_id)
end

select dbo.question1(2) as price

select list_price from production.products where product_id = 2


/*
Write an inline table-valued function
that returns all products for a given category_id.
*/

alter function fn_question2(@cat_id int)
returns table
as
return (select top 10 * from production.products where category_id=@cat_id)

select * from dbo.fn_question2(3)

/*
Create a function that takes a store_id and 
returns the total sales amount for that store.
Use the sales.orders and sales.order_items tables. 
Sum the list_price * quantity for all orders from that store.
*/

create function fn_question3(@str_id int)
returns decimal(10,2)
as
begin
declare @total decimal(10,2)
select @total =sum(oi.list_price * oi.quantity) from sales.orders o join sales.order_items oi
on o.order_id= oi.order_id
where o.store_id = @str_id
return @total
end

select dbo.fn_question3(1) as total


/*
Write a table-valued function that takes two dates as input 
and returns all orders placed between those dates.
*/

create function fn_question4(@startdate date,@enddate date)
returns table
as
return (select * from sales.orders where order_date between @startdate and @enddate)

select top 10 * from dbo.fn_question4('2018-01-01','2018-02-01')


/*
Write a function that takes a brand_id 
and returns the number of products for that brand.
*/

create function fnn_question5(@b_id int)
returns int
as
begin
declare @count int
select @count=count(product_id) from production.products where brand_id = @b_id
return @count
end

select dbo.fnn_question5(2) as count_of_products
