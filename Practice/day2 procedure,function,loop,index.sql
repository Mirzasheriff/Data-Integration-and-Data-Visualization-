use stored_pc

create table employees
(
id int primary key,
name varchar(50),
gender varchar(50),
DOB datetime,
DeptID int
)

INSERT INTO Employees VALUES
(1, 'Geetha', 'Female', '1996-02-29', 1),
(2, 'Fransy', 'Female', '1995-05-25', 2),
(3, 'Gopi', 'Male', '1995-04-19', 2),
(4, 'BanuRekha', 'Female', '1996-03-17', 3),
(5, 'Shalini', 'Female', '1997-01-15', 1),
(6, 'Kalai', 'Female', '1995-07-12', 2),
(7, 'Santosh', 'Male', '1994-10-10', 1),
(8, 'Hariharan', 'Male', '1993-08-21', 2);

--simple procedure--

create procedure usp_getallemp
as
begin
select * from employees
end

execute usp_getallemp
exec usp_getallemp
usp_getallemp


--procedure with parameter--

alter procedure usp_getallempbydept(@dept int)
as
begin
select * from employees where deptid = @dept
end

exec usp_getallempbydept 2

--procedure with multiple paramter--

create proc usp_getdeptandgender (@deptid int, @gender varchar(10))
as
begin
select * from employees where deptid = @deptid and gender= @gender
end

exec usp_getdeptandgender @deptid = 2,@gender='male'
exec usp_getdeptandgender 2,'male'

--procedure with output--

create procedure addition(@num1 int,@num2 int,@num3 int output)
as
begin
set @num3=@num1+@num2
end

declare @sum int
exec addition 10,20,@sum output
print @sum

--returning using output for multiple datas--

create procedure gendercount (@malecount int out, @femalecount int out)
as
begin
select @malecount=count(*) from employees where gender= 'male'
select @femalecount=count(*) from employees where gender = 'female'
end

declare @malecount int,@femalecount int
exec gendercount @malecount out,@femalecount out
print 'female: ' +cast(@femalecount as varchar(10)) +', male: ' + cast(@malecount as varchar(10))

--employee count by gender --

create procedure specificgendercount(@gender varchar(10), @empcount int out)
as
begin
select @empcount=count(ID) from employees where gender = @gender
end

declare @gender varchar(10), @empcount int
exec specificgendercount @gender='Female',@empcount=@empcount out
print @empcount
--or--
declare @empcount int
exec specificgendercount 'Female',@empcount out
print @empcount
--coz above if its name= value, then all datas must be in that way-- 




--proc for multiple data output--

create proc mult_data (@dept int,@name varchar(50) out, @DOB varchar(50) out)
as
begin
select @name=name,@DOB=DOB from employees where deptid= @dept
end

declare @name varchar(50),@DOB varchar(50)
exec mult_data 2,@name out,@DOB out
print 'Name is '+@name+' and the DOB is '+@DOB

--above only gives you one row ,that too only last found row=--


--below gives you all rows that match the query condition--

create proc mult_data1 (@dept int)
as
begin
select name,DOB from employees where deptid= @dept
end

exec mult_data1 1

sp_helptext mult_data1

--encrypting query--

create proc mult_data2 (@dept int)
with encryption --query encrypted
as
begin
select name,DOB from employees where deptid= @dept
end

exec mult_data2 2


--default paramtere proc--

create proc mult_data3 (@dept int=3)
with encryption --query encrypted
as
begin
select name,DOB from employees where deptid= @dept
end

exec mult_data3 2
exec mult_data3 

select * from employees




--======FUNCTIONS========--



--scalar values function--

create function cubing(@num int) 
returns int
as
begin
return @num*@num*@num
end


select dbo.cubing(3)

/*
scalar value function
returns single value like aggregate(min,max,avg...)
*/


--Inline table values function--

create function get_all_data_emp(@deptid int)
returns table
as
return (select id,name,gender from employees where deptid = @deptid)

/*
body of function will have only a single select,
return type as table,
no begin or ends since returns only single select
*/
select * from dbo.get_all_data_emp(1)



--Multi statement table valued function--

create function multi_table(@deptid int)
returns @MyTable Table(id int,name varchar(50),gender varchar(30),DOB varchar(30))
as 
begin
insert into @MyTable
select id,name,gender,DOB from employees where deptid=@deptid
return
end

/*
More than one statement can be used,
returns table,
uses begin,end
*/

select * from dbo.multi_table(2)




--==Assignment==============-

/*
Write a scalar-valued function that 
takes a product_id as input and 
returns the list_price of that product.
*/






--=============index sql=================--

CREATE TABLE financial_transactions (
    transaction_id INT ,
    customer_id INT,
    supplier_name VARCHAR(50),
    transaction_date DATE,
    amount DECIMAL(10, 2),
    currency VARCHAR(10)
);


CREATE TABLE tbl_Employee
(
Id INT,
Name VARCHAR(50),
Salary INT,
Gender VARCHAR(10),
City VARCHAR(50),
Dept VARCHAR(50)
)
GO

INSERT INTO tbl_Employee VALUES (3,'Pranaya', 4500, 'Male', 'New York', 'IT')
INSERT INTO tbl_Employee VALUES (1,'Anurag', 2500, 'Male', 'London', 'IT')
INSERT INTO tbl_Employee VALUES (4,'Priyanka', 5500, 'Female', 'Tokiyo', 'HR')
INSERT INTO tbl_Employee VALUES (5,'Sambit', 3000, 'Male', 'Toronto', 'IT')
INSERT INTO tbl_Employee VALUES (7,'Preety', 6500, 'Female', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (6,'Tarun', 4000, 'Male', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (2,'Hina', 500, 'Female', 'Sydney', 'HR')
INSERT INTO tbl_Employee VALUES (8,'John', 6500, 'Male', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (10,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (9,'Sara', 500, 'Female', 'London', 'IT')

select * from tbl_Employee where Id=5

create clustered index idx_Emplioyee_Id on tbl_Employee(Id)
--sorted based on id

drop index idx_Emplioyee_Id on tbl_Employee

truncate table tbl_Employee

create nonclustered index idx_id on tbl_Employee(Id)
--sort reflected in result set but not in physical table

drop index idx_employee_id on tbl_Employee

create unique index idx_unique_id on tbl_Employee(Id)



--T-SQL
/*
How to declare the variable
Loop
*/

CREATE Table tblOrder
(Id INT,
CustomerId INT,
ProductID varchar(50),
ProductName varchar(50)
)

declare @i int=1
while @i<=4000
begin
    if(@i<1000)
    begin
	INSERT INTO tblOrder values (@i,1,'Product-101','iPad Air')
	END
	ELSE IF(@i<2000)
	BEGIN
	INSERT INTO tblOrder values (@i,3,'Product-3001','Lenova Think Pad')
	END
	ELSE IF(@i<3000)
	BEGIN
	INSERT INTO tblOrder values (@i,2,'Product-100','Wireless Keyboard')
	END
	ELSE IF(@i<=4000)
	BEGIN
	INSERT INTO tblOrder values (@i,1,'Product-300','Tablet')
	END
	SET @i=@i+1
END

select count(*) from tblOrder

truncate table tblOrder

SELECT * FROM tblOrder WHERE ProductID='Product-3001' AND CustomerId=3


CREATE NONCLUSTERED INDEX idx_tblOrder_pid
ON tblOrder(ProductId)
INCLUDE([Id],[CustomerId],[ProductName])

SELECT * FROM tblOrder WHERE ProductID='Product-100'
