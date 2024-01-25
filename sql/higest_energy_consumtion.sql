-- Find the date with the highest total energy consumption from the Meta/Facebook data centers. 
-- Output the date along with the total energy consumption across all data centers.
-- Tables: fb_eu_energy, fb_asia_energy, fb_na_energy

with cte as (
select date, consumption from fb_eu_energy
union all
select date, consumption from fb_asia_energy
union all
select date, consumption from fb_na_energy
order by date
),
subtt as (
select date, sum(consumption) as tt
from cte
group by date
),
rnk as (
select date, tt, DENSE_RANK() OVER (order BY tt desc) as pstn
from subtt
)
select date, tt as consumption
from rnk
where pstn = 1