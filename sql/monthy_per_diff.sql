-- Given a table of purchases by date, calculate the month-over-month percentage change in revenue. 
-- The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, 
-- and sorted from the beginning of the year to the end of the year.
-- The percentage change column will be populated from the 2nd month forward 
-- and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.

-- id	created_at	value	purchase_id
-- 1	2019-01-01	172692	43
-- 2	2019-01-05	177194	36
-- 3	2019-01-09	109513	30
-- 4	2019-01-13	164911	30
-- 5	2019-01-17	198872	39

with cte as (
select
    date_format(created_at, '%Y-%m') as ym,
    sum(value) as tt_rev
from sf_transactions
group by 1
order by 1
)
select ym,
    round(((tt_rev - (lag(tt_rev)over())) / (lag(tt_rev)over())) * 100, 2) as revenue_diff_pct
from cte