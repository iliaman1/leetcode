-- SQL Schema
Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int)
Truncate table Queue
insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1')
insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5')
insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2')
insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3')
insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6')
insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4')

-- Write your PostgreSQL query statement below
SELECT person_name
FROM (
    SELECT person_id,
           person_name,
           SUM(weight) OVER (ORDER BY turn) AS cum_sum
     FROM Queue
     ORDER BY turn DESC
)
WHERE cum_sum <= 1000
LIMIT 1