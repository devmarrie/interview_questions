-- Find the percentage of shipable orders.

-- Consider an order is shipable if the customer's address is known.
-- Tables: orders, 
-- id:int
-- cust_id:int
-- order_date:date
-- timeorder_details:varchar
-- total_order_cost:int

-- customers
-- id:int
-- first_name:varchar
-- last_name:varchar
-- city:varchar
-- address:varchar
-- phone_number:varchar

with adrs as (
select count(*) as wale
from orders o
inner join customers c
on o.cust_id = c.id
where c.address != ' '
),
tt as (
select count(*)  as wote 
from orders o
inner join customers c
on o.cust_id = c.id
)
select (wale / wote) * 100 AS percent_shipable
from adrs, tt;
