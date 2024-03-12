-- Find employees who are earning more than their managers. 
-- Output the employee's first name along with the corresponding salary.
-- Table: employee

with cte as (
select  distinct e.id, e.first_name as mng, e.salary as mng_sal
from employee e
inner join employee m
on e.id = m.manager_id
)
select e.first_name, e.salary
from employee e
inner join cte m
on e.manager_id = m.id
where e.salary > m.mng_sal