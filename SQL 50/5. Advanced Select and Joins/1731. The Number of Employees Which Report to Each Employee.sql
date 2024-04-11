-- SQL Schema
Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
Truncate table Employees
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', 'None', '43')
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', 'None', '37')

-- Write your PostgreSQL query statement below JOIN
SELECT
    m.employee_id,
    m.name,
    count(*) AS reports_count,
    round(avg(e.age)) AS average_age
FROM
    Employees e
    JOIN Employees m ON e.reports_to = m.employee_id
GROUP BY
    m.employee_id,
    m.name
ORDER BY
    m.employee_id;

-- Write your PostgreSQL query statement below Subquery
SELECT
    e.reports_to AS employee_id,
    (SELECT name FROM Employees WHERE employee_id = e.reports_to),
    count(*) AS reports_count,
    round(avg(e.age)) AS average_age
FROM
    Employees e
WHERE
    e.reports_to IS NOT NULL
GROUP BY
    e.reports_to
ORDER BY
    e.reports_to;