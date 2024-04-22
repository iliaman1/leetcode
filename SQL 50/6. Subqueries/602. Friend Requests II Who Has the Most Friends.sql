-- SQL Schema
Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null)
Truncate table RequestAccepted
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09')

-- Write your PostgreSQL query statement below
WITH CountOfFriends AS
(
    SELECT requester_id as id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id
    FROM RequestAccepted
)

SELECT id, COUNT(id) as num
FROM CountOfFriends
GROUP BY id
ORDER BY num DESC
LIMIT 1