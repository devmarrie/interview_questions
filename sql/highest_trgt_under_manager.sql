-- Find the highest target achieved by the employee or employees who works under the manager id 13. 
-- Output the first name of the employee and target achieved. 
-- The solution should show the highest target achieved under manager_id=13 and which employee(s) achieved it.
-- Table: salesforce_employees

with cte as (
select first_name, target, 
dense_rank()over(order by target desc) as rnk
from salesforce_employees
where manager_id = 13
)

select first_name, target
from cte
where rnk = 1