-- SQL Schema
Create table If Not Exists Users (user_id int, name varchar(40))
Truncate table Users
insert into Users (user_id, name) values ('1', 'aLice')
insert into Users (user_id, name) values ('2', 'bOB')

-- Write your PostgreSQL query statement below
SELECT user_id, concat(upper(substr(name, 1, 1)), lower(substr(name,2,length(name)))) as name
FROM Users
ORDER BY user_id;