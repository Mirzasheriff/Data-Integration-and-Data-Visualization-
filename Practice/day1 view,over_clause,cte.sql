create database sampledb

use sampledb

create table department(id int primary key, name varchar(50) )
go

select * from department

insert into department(id,name) values (1,'IT')
insert into department(id,name) values (2,'HR')
insert into department(id,name) values (3,'Sales')

create table employee(
id int primary key,
name varchar(50),
gender varchar(50),
DOB datetime,
deptid int
)

select * from dbo.employee

insert into employee(id,name,gender,DOB,deptid) values(1,'Sheriff','Male','2003-04-08',1)
insert into employee(id,name,gender,DOB,deptid) values(2,'Ibrahim','Male','2004-07-22',2)
insert into employee(id,name,gender,DOB,deptid) values(3,'Harsha','Female','2002-02-26',3)
insert into employee(id,name,gender,DOB,deptid) values(4,'Rishi','Male','2003-06-25',1)
insert into employee(id,name,gender,DOB,deptid) values(5,'Aaron','Male','2003-08-16',2)
insert into employee(id,name,gender,DOB,deptid) values(6,'Alia','Female','2003-08-16',3)
insert into employee(id,name,gender,DOB,deptid) values(7,'Amrin','Female','2003-08-16',1)
insert into employee(id,name,gender,DOB,deptid) values(8,'Asmitha','Female','2003-08-16',3)


create view
vwgetallemp 
as select * from employee where gender='Female'

select * from vwgetallemp

insert into vwgetallemp(id,name,gender,DOB,deptid) values (9,'Safia','Female','2005-09-08',3)

create view 
vwallemp 
as select e.id,e.gender,e.DOB,d.name from employee e join department d 
on d.id = e.deptid

select * from vwallemp

insert into vwallemp(id,name,gender,DOB,deptid) values (11,'Fary','Female','2005-09-08',1)

create view vwdept
as
select * from department

select * from vwdept

create table school(id int primary key, name varchar(50) )
go

insert into school(id,name) values (1,'IT')
insert into school(id,name) values (2,'HR')
insert into school(id,name) values (3,'Sales')

select * from school

create view vwdeptcheck
as
select * from school

select * from vwdeptcheck

alter view vwdeptcheck
as
select * from school
with check option

insert into novwdeptcheck(id,name) values(5,'also-Management')

insert into vwdeptcheck(id,name) values(11,'staff')

sp_helptext vwdeptcheck

alter view vwdeptcheck as
select * from school where id<3
with check option

sp_helptext vwdeptcheck

alter view vwdeptcheck
with encryption
as
select * from school where id<3
with check option

create view vwemp 
with encryption
as select * from employee where gender = 'Male'
with check option

select * from vwemp

insert into vwemp(id,name,gender,DOB,deptid) values(16,'Judith','Female','2004-01-01',3)

update vwemp set id = 11 where name= 'Judith'

--cte--

create table employees(
id int primary key,
name varchar(30),
department varchar(10),
salary int
)
go

select * from employees

Insert Into Employees Values (1, 'James', 'IT', 80000)
Insert Into Employees Values (2, 'Taylor', 'IT', 80000)
Insert Into Employees Values (3, 'Pamela', 'HR', 50000)
Insert Into Employees Values (4, 'Sara', 'HR', 40000)
Insert Into Employees Values (5, 'David', 'IT', 35000)
Insert Into Employees Values (6, 'Smith', 'HR', 65000)
Insert Into Employees Values (7, 'Ben', 'HR', 65000)
Insert Into Employees Values (8, 'Stokes', 'IT', 45000)
Insert Into Employees Values (9, 'Taylor', 'IT', 70000)
Insert Into Employees Values (10, 'John', 'IT', 68000)
Go

with highsalary_cte as 
(
select id,name,department,salary from employees where salary>=80000
)
select * from highsalary_cte


select * from employees

--over clause--

select department,count(*) as total_emp,
sum(salary) as tot_salary,
max(salary) as max_Salary,
min(salary) as min_salary,
avg(salary) as average_salary
from employees
group by department

--we cant use non aggregate data like name above so we use joins.. but there 
--is a better option--in easy way--over clause

select name,salary,department,
count(department) over(partition by department) as no_of_emp,
max(salary) over(partition by department) as max_salary,
min(salary) over(partition by department) as min_salary,
avg(salary) over(partition by department) as avg_salary
from employees



select name,salary,e.department,d.totalemp.d.totalsal,d.minsal,d.maxsal,d.avgsal
from employees e inner join
(
select department,
count(*) as totalemp,
min(salary) as minsal,
max(salary) as maxsal,
avg(salary) as avgsal
from employees group by department )d on d.department= e.department


SELECT Name,Salary,E.Department,
d.TotalEmployees,
d.TotalSalary,
d.MinSalary,
d.MaxSalary,
d.AverageSalary
FROM employees e
INNER Join(
SELECT Department,
count(*)  as TotalEmployees,
sum(salary) as TotalSalary,
min(salary) as MinSalary,
Max(salary) as MaxSalary,
Avg(Salary) as AverageSalary
FROM Employees 
Group BY Department)
d on d.Department=e.Department


with deleteduplicate_cte as
(
select *,ROW_NUMBER() over (partition by department order by id) as row_numbers
from employees
)
delete from deleteduplicate_cte where row_numbers>1

select * from employees

select * from employee

with seeduplicate_cte as 
(
select *,ROW_NUMBER() over (partition by gender order by deptid) as row_numbers
from employee
)select * from seeduplicate_cte

truncate table employees

INSERT INTO Employees VALUES
(1, 'James', 'IT', 80000),
(2, 'Taylor', 'IT', 80000),
(3, 'Pamela', 'HR', 50000),
(4, 'Sara', 'HR', 40000),
(5, 'David', 'IT', 35000),
(6, 'Smith', 'HR', 65000),
(7, 'Ben', 'HR', 65000),
(8, 'Stokes', 'IT', 45000),
(9, 'Taylor', 'IT', 70000),
(10, 'John', 'IT', 68000);

select * from employees


select *,
DENSE_RANK() over (partition by department order by salary desc) as dense_ranks
from employees

with empctc_cte as(
select *,dense_rank() over (partition by department order by salary desc) as ranks
from employees)
select * from empctc_cte
