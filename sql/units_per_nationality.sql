-- Find the number of apartments per nationality that are owned by people under 30 years old.

-- Output the nationality along with the number of apartments.

-- Sort records by the apartments count in descending order.
-- Tables: airbnb_hosts, airbnb_units

with cte as (
select distinct h.nationality,
    u.unit_id
from airbnb_hosts h
left join airbnb_units u
on h.host_id = u.host_id
where h.age < 30 and u.unit_type = 'Apartment'
)
select nationality,
    count(unit_id) as apartment_count
from cte
group by nationality
order by count(unit_id) desc