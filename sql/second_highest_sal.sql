-- Find the second highest salary of employees.
-- Table: employee

with cte as (
select distinct first_name, salary,
    dense_rank()over(order by salary desc) as rnk
from employee
order by salary desc
)
select salary
from cte
where rnk = 2