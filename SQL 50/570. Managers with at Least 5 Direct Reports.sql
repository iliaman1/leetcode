-- SQL Schema
Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int)
Truncate table Employee
insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', 'None')
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101')
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101')
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101')
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101')
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101')

-- Write your PostgreSQL query statement below
select name
from Employee e
inner join (select managerId from Employee group by managerId having(count(distinct id)) >= 5) r
on e.id = r.managerid;

-- Write your PostgreSQL query statement below
select name
from Employee
where id in (select managerId from Employee group by managerId having(count(distinct id)) >= 5);