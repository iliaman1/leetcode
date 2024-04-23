-- SQL Schema
Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float)
Truncate table Insurance
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40')

-- Write your PostgreSQL query statement below
WITH unique_tiv2016 AS (
    SELECT MIN(pid) AS pid,
            MIN(tiv_2016) AS tiv_2016,
            MIN(tiv_2015) AS tiv_2015
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(pid) = 1
)

SELECT ROUND(SUM(t1.tiv_2016)::decimal, 2) AS tiv_2016
FROM unique_tiv2016 AS t1
WHERE EXISTS (
            SELECT 1
            FROM Insurance AS i
            WHERE i.pid != t1.pid
                AND i.tiv_2015 = t1.tiv_2015);