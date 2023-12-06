-- Write a query that'll identify returning active users. 
-- A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. 
-- Output a list of user_ids of these returning active users.
-- id	user_id	item	created_at	revenue
-- 1	109	milk	2020-03-03	123
-- 2	139	biscuit	2020-03-18	421
-- 3	120	milk	2020-03-18	176
-- 4	108	banana	2020-03-18	862
-- 5	130	milk	2020-03-28	333

-- first approach
-- with cte as(
-- select user_id, created_at, 
--     lag(created_at) over(partition by user_id order by created_at) as prev
-- from amazon_transactions 
-- )
-- select distinct u.user_id
-- from cte u
-- where u.created_at <= u.prev + interval '7' day
--     and u.prev is not null;

--using lead
with cte as(
select user_id, created_at, 
    lead(created_at) over(partition by user_id order by created_at) as prev
from amazon_transactions 
)
select distinct u.user_id
from cte u
where u.prev - u.created_at <= 7
    and u.prev is not null;