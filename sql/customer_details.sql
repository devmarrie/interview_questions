-- Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details.
-- You may have duplicate rows in your results due to a customer ordering several of the same items. Sort records based on the customer's first name and the order details in ascending order.
-- Tables: customers, orders

select c.first_name, c.last_name, c.city, d.order_details
from customers c
left join orders d
on c.id = d.cust_id 
order by c.first_name, d.order_details;