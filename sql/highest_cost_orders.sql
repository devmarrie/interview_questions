-- Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If customer had more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total cost of their items, and the date.

-- For simplicity, you can assume that every first name in the dataset is unique.
-- Tables: customers, orders

select c.first_name, o.order_date, sum(o.total_order_cost) as total_cost
from customers c
inner join orders o
on c.id = o.cust_id
where o.order_date >= '2019-02-01' and o.order_date <= '2019-05-01'
group by o.order_date, c.first_name
limit 1;