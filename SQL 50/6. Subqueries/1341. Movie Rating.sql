-- SQL Schema
Create table If Not Exists Movies (movie_id int, title varchar(30))
Create table If Not Exists Users (user_id int, name varchar(30))
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date)
Truncate table Movies
insert into Movies (movie_id, title) values ('1', 'Avengers')
insert into Movies (movie_id, title) values ('2', 'Frozen 2')
insert into Movies (movie_id, title) values ('3', 'Joker')
Truncate table Users
insert into Users (user_id, name) values ('1', 'Daniel')
insert into Users (user_id, name) values ('2', 'Monica')
insert into Users (user_id, name) values ('3', 'Maria')
insert into Users (user_id, name) values ('4', 'James')
Truncate table MovieRating
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22')
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25')

-- Write your PostgreSQL query statement below
WITH movierating_in_february_2020 AS (
    SELECT *
    FROM MovieRating
    WHERE TO_CHAR(created_at, 'yyyy-mm') = '2020-02'
),

movie_title_with_highest_average_rating_in_february_2020 AS (
    SELECT title
    FROM movierating_in_february_2020
    INNER JOIN Movies
    USING(movie_id)
    GROUP BY movie_id, title
    ORDER BY AVG(rating) DESC,
            title ASC
    LIMIT 1
),

user_name_who_has_rated_the_greatest_number_of_movies AS (
    SELECT name
    FROM MovieRating
    INNER JOIN Users
    USING(user_id)
    GROUP BY user_id, name
    ORDER BY COUNT(movie_id) DESC,
            name ASC
    LIMIT 1
)

SELECT name AS results
FROM user_name_who_has_rated_the_greatest_number_of_movies

UNION ALL

SELECT title
FROM movie_title_with_highest_average_rating_in_February_2020;