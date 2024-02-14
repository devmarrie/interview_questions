-- Find the top 5 states with the most 5 star businesses. 
-- Output the state name along with the number of 5-star businesses and 
-- order records by the number of 5-star businesses in descending order. 
-- In case there are ties in the number of businesses, return all the unique states. 
-- If two states have the same result, sort them in alphabetical order.
-- Table: yelp_business
-- Expected Output:
-- state	five_star_counts
-- AZ	10
-- ON	5
-- NV	4
-- IL	3
-- OH	3

with cte as(
select state, count(stars) as stars 
from yelp_business
where stars = 5
group by state
order by stars desc
), 
r as (
select state, stars,
  dense_rank() over (order by stars desc) as rnk
from cte
)
select state, stars as five_star_counts
from r
where rnk <= 4
order by stars desc, state asc
