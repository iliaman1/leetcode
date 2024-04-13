-- SQL Schema
Create table If Not Exists Triangle (x int, y int, z int)
Truncate table Triangle
insert into Triangle (x, y, z) values ('13', '15', '30')
insert into Triangle (x, y, z) values ('10', '20', '15')

-- Write your PostgreSQL query statement below
SELECT x, y, z, (CASE WHEN x+y+z > 2*GREATEST(x, y, z) THEN 'Yes' ELSE 'No' END) AS triangle
FROM Triangle;

-- Without function
SELECT x, y, z, (CASE WHEN x < y + z and y < x + z and z < x + y THEN 'Yes' ELSE 'No' END) AS triangle
FROM Triangle;