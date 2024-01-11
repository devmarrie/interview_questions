-- Find the number of Apple product users and the number of total users with a device and group the counts by language. 
-- Assume Apple products are only MacBook-Pro, iPhone 5s, and iPad-air. 
-- Output the language along with the total number of Apple users and users with any device. 
-- Order your results based on the number of total users in descending order.
-- Tables: playbook_events, playbook_users.

-- Expected Output
-- language	n_apple_user	n_total_users
-- english	    11	                45
-- spanish	    3	                9
-- japanese	2	                6
-- french	    0	                5
-- russian	    0	                5

with apple as (
select  distinct e.user_id, e.device, u.language
from playbook_events e
inner join playbook_users u
on e.user_id = u.user_id
where e.device = 'macbook pro' or e.device = 'iPhone 5s' or e.device = 'ipad air'
), 
ttl as (
select  distinct e.user_id,  u.language
from playbook_events e
inner join playbook_users u
on e.user_id = u.user_id
),
au as (
select language, count(*) as n_apple_user
from apple
group by language
order by count(*) desc
),
ttu as (
select language, count(*) as n_total_users
from ttl
group by language
order by count(*) desc
)
select t.language, coalesce(u.n_apple_user, 0) as n_apple_user, t.n_total_users
from ttu as t
left join au u
on t.language = u.language
order by t.n_total_users desc
