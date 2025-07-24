create database tr
use tr

CREATE TABLE tblEmployee
(
  Id int Primary Key,
  Name nvarchar(30),
  Salary int,
  Gender nvarchar(10),
  DepartmentId int
)

Insert into tblEmployee values (1,'John', 5000, 'Male', 3)
Insert into tblEmployee values (2,'Mike', 3400, 'Male', 2)
Insert into tblEmployee values (3,'Pam', 6000, 'Female', 1)

CREATE TABLE tblEmployeeAudit
(
  Id int identity(1,1) primary key,
  AuditData nvarchar(1000)
)

SELECT * FROM tblEmployee
SELECT * from tblEmployeeAudit

--Trigger to notify that a employee has been added
--after trigger or for trigger
create trigger trg_after_insert_employee
on tblEmployee
after insert
as
begin
print 'Record inserted in tblEmployee'
end

INSERT INTO tblEmployee VALUES
(4,'MD',65000,'male',1)

drop trigger trg_after_insert_employee

--detailled notification of data and appending to audit table

create trigger tr_tblEmployee_forinsert
on tblEmployee
after insert
as
begin
declare @Id int
select @Id = Id from inserted

insert into tblEmployeeAudit values('New emp with id: '
+ cast(@Id as varchar(5))+ ' is added at '+cast(getdate() as nvarchar(20)))
end

drop trigger tr_tblEmployee_forinsert

INSERT INTO tblEmployee VALUES
(6,'Sharan',45000,'male',2)

--instead of trigger
--restricting permission to insert

create trigger trg_insteadofinsert_Employee
on tblEmployee
instead of insert
as
begin
print'Insertion of employee denied'
rollback
end

drop trigger trg_insteadofinsert_Employee


INSERT INTO tblEmployee VALUES
(5,'MS',75000,'female',2)


select GETDATE()






--complex trigger for update:for--

create trigger tr_tblEmployee_forupdate
on tblEmployee
for Update
as
begin

--declaring variables to hold old and new data--
declare @Id int
Declare @oldname nvarchar(20), @newname nvarchar(20)
declare @oldsalary int, @newsalary int
declare @oldgender nvarchar(20), @newgender nvarchar(20)
declare @olddeptid int,@newdeptid int

--variable to build the audit string--
declare @auditstring nvarchar(800)

-- Load the updated records into temporary table--
select * into #TempTable from inserted

--looping through table as it may have more than one row
while(Exists(select Id from #TempTable))
begin

--emptying audit string
set @auditstring = ''

--selecting first row from temptable--
select top 1 @Id= Id, @newname = Name, @newgender = gender,
@newsalary = salary, @newdeptid = DepartmentId
from #TempTable

--selecting the corresponding row from deleted table--
select @oldname= Name,@oldgender = gender, @oldsalary = salary,
@olddeptid = DepartmentId from deleted where Id = @Id

 -- Build the audit string dynamically--
 set @auditstring = 'Employee with id: '+cast(@Id as nvarchar(4)) +' changed '
 if(@oldname <> @newname)
     set @auditstring = @auditstring+ 'name from '+@oldname+' to '+@newname

 if(@oldgender <> @newgender)
     set @auditstring = @auditstring+ 'gender from '+@oldgender+' to '+@newgender

 if(@oldsalary <> @newsalary)
     set @auditstring = @auditstring+ 'salary from '+
     cast(@oldsalary as nvarchar(20))+' to '+cast(@newsalary as nvarchar(20))

 if(@olddeptid <> @newdeptid)
     set @auditstring = @auditstring+ 'DeptId from '+
     cast(@olddeptid as nvarchar(10))+' to '+cast(@newdeptid as nvarchar(10))

insert into tblEmployeeAudit values(@auditstring)

delete from #TempTable where Id= @Id

end
end




--now test the above code-

update tblEmployee set name = 'SheriffIbrahim' where Id=1

update tblEmployee set gender = 'female' where Id = 2

update tblEmployee set gender = 'male' where Id = 2

insert into tblEmployee values(5,'Hari',7000,'male',3)

insert into tblEmployee values(7,'ina',12000,'male',2)






--===================TRANSACTION QUERIES======================--

CREATE TABLE Product (
    ProductID INT PRIMARY KEY, 
    Name VARCHAR(40), 
    Price INT,
    Quantity INT
)

-- Inserting 4 rows
INSERT INTO Product VALUES(101, 'Product-1', 100, 10)
INSERT INTO Product VALUES(102, 'Product-2', 200, 15)
INSERT INTO Product VALUES(103, 'Product-3', 300, 20)
INSERT INTO Product VALUES(104, 'Product-4', 400, 25)


select * from product


--success transaction--
BEGIN TRANSACTION
    INSERT INTO Product VALUES(105,'Product-5',500, 30)
    UPDATE Product SET Price =350 WHERE ProductID = 103
    DELETE FROM Product WHERE ProductID = 103
COMMIT TRANSACTION



--failed transaction--
BEGIN TRANSACTION
BEGIN TRY
    INSERT INTO Product VALUES(106,'Product-6',600,12)
    INSERT INTO Product VALUES(106,'Product-6',600,12) -- DUPLICATE PRIMARY KEY
    DELETE FROM Product where ProductID=102
    COMMIT TRANSACTION
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION
END CATCH



SET IMPLICIT_TRANSACTIONS ON--u need to manually commit hereby



CREATE TABLE Customer (
    CustomerId int primary key,
    CustomerCode varchar(10),
    CustomerName varchar(50)
)

select * from customer

-- Will FAIL because of duplicate key (CustomerId = 1 twice)
insert into Customer values(1,'ccode-1','John')
insert into Customer values(1,'ccode-2','James')
--fails
insert into Customer values(2,'ccode-1','John')
insert into Customer values(2,'ccode-2','James')

truncate table customer



SET IMPLICIT_TRANSACTIONS ON
insert into Customer values(1,'ccode-1','John')
insert into Customer values(2,'ccode-2','James')
COMMIT Transaction


insert into Customer values(3,'ccode-3','Peter')
update Customer set CustomerName='Riya' where CustomerId=1
ROLLBACK TRANSACTION




SET IMPLICIT_TRANSACTIONS ON
INSERT INTO Customer VALUES(4, 'ccode-4', 'Alice')
-- Don't commit
SELECT * FROM Customer  -- The row is inserted **but not committed yet**
ROLLBACK TRANSACTION
SELECT * FROM Customer  -- The row should now be gone



SET IMPLICIT_TRANSACTIONS OFF
INSERT INTO Customer VALUES(4, 'ccode-4', 'Alice')
-- Don't commit
SELECT * FROM Customer  -- The row is inserted **but not committed yet**
ROLLBACK TRANSACTION
SELECT * FROM Customer  -- The row should now be gone


-- Step 1: Enable implicit
SET IMPLICIT_TRANSACTIONS OFF

-- Step 2: Insert without committing
INSERT INTO Customer VALUES (6, 'ccode-5', 'Sam')

-- Step 3: Open a **NEW SSMS window** and run:
SELECT * FROM Customer


