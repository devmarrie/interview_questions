-- Meta/Facebook has developed a new programing language called Hack.
-- To measure the popularity of Hack they ran a survey with their employees. 
-- The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with 
-- Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.
-- Based on the above, find the average popularity of the Hack per office location.
-- Output the location along with the average popularity.
-- Tables: facebook_employees, facebook_hack_survey
-- location	avg_popularity
-- USA	        4.6
-- India	    7.5
-- UK	        4.333
-- Switzerland	1

with cte as (
select e.id, e.location, h.popularity
from facebook_employees e
inner join facebook_hack_survey h
on e.id = employee_id
)
select location, avg(popularity) as avg_popularity
from cte
group by location