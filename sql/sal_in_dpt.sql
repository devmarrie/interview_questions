-- Find the employee with the highest salary per department.
-- Output the department name, employee's first name along with the corresponding salary.
-- Table: employee

with cte as (
select first_name, department, salary, 
dense_rank()over(partition by department order by salary desc) as rnk
from employee
order by department, salary desc
)
select department, first_name as employee_name, salary
from cte
where rnk = 1
order by salary desc