-- SQL Schema
Create table If Not Exists Seat (id int, student varchar(255))
Truncate table Seat
insert into Seat (id, student) values ('1', 'Abbot')
insert into Seat (id, student) values ('2', 'Doris')
insert into Seat (id, student) values ('3', 'Emerson')
insert into Seat (id, student) values ('4', 'Green')
insert into Seat (id, student) values ('5', 'Jeames')

-- Write your PostgreSQL query statement below
SELECT CASE WHEN id%2=0 THEN id-1
WHEN id%2=1 AND id<(SELECT max(id) FROM Seat) THEN id+1 ELSE id END id, student
FROM Seat
ORDER BY id;
