-- Find the top 5 businesses with most reviews. Assume that each row has a unique business_id such that the total reviews for each business is listed on each row. 
-- Output the business name along with the total number of reviews and order your results by the total reviews in descending order.
with cte as(
select name, sum(review_count) over (partition by name) as review_count
from yelp_business
),
r as (
select name, review_count, rank() over(order by review_count desc) as rnk
from cte
)
select name, review_count
from r
where rnk <= 5;
