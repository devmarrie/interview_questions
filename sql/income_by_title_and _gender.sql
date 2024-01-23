-- Find the average total compensation based on employee titles and gender. Total compensation is calculated by adding both the salary and bonus of each employee. However, not every employee receives a bonus so disregard employees without bonuses in your calculation. Employee can receive more than one bonus.
-- Output the employee title, gender (i.e., sex), along with the average total compensation.
-- Tables: sf_employee, sf_bonus

with cte as (
select e.id, e.sex, e.salary, e.employee_title, sum(b.bonus) as bonus
from sf_employee e
inner join sf_bonus b
on e.id = b.worker_ref_id
group by 1
)
select employee_title, sex, avg(salary + bonus) as avg_compensation
from cte 
group by employee_title, sex