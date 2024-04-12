-- SQL Schema
Create table If Not Exists Employee (employee_id int, department_id int, primary_flag ENUM('Y','N'))
Truncate table Employee
insert into Employee (employee_id, department_id, primary_flag) values ('1', '1', 'N')
insert into Employee (employee_id, department_id, primary_flag) values ('2', '1', 'Y')
insert into Employee (employee_id, department_id, primary_flag) values ('2', '2', 'N')
insert into Employee (employee_id, department_id, primary_flag) values ('3', '3', 'N')
insert into Employee (employee_id, department_id, primary_flag) values ('4', '2', 'N')
insert into Employee (employee_id, department_id, primary_flag) values ('4', '3', 'Y')
insert into Employee (employee_id, department_id, primary_flag) values ('4', '4', 'N')

-- Write your PostgreSQL query statement below
WITH employee_id_with_number_of_department AS (
    SELECT employee_id, COUNT(department_id) AS number_of_department
    FROM Employee
    GROUP BY employee_id
)

SELECT e.employee_id, department_id
FROM Employee AS e
INNER JOIN employee_id_with_number_of_department AS prime
ON e.employee_id = prime.employee_id
        AND (number_of_department = 1 OR primary_flag = 'Y');