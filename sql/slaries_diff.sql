-- Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
-- Output just the absolute difference in salaries.
-- db_employee
-- id	first_name	last_name	salary	department_id
-- 10301	Keith	Morgan	27056	2
-- 10302	Tyler	Booth	32199	3
-- 10303	Clifford	Nguyen	32165	2
-- 10304	Mary	Jones	49488	3
-- 10305	Melissa	Lucero	27024	3

-- db_dept
-- id	department
-- 1	engineering
-- 2	human resource
-- 3	operation
-- 4	marketing
-- 5	sales

-- Output
-- salary_difference
-- 2400

with mkt as (
select e.salary, dpt.department,
    rank()over(order by e.salary desc) as rnk
from db_employee e
inner join db_dept dpt
on e.department_id = dpt.id
where dpt.department = 'marketing'
limit 1
),
eng as (
select e.salary, dpt.department,
    rank()over(order by e.salary desc) as rnk
from db_employee e
inner join db_dept dpt
on e.department_id = dpt.id
where dpt.department = 'engineering'
limit 1
)
select m.salary - e.salary as salary_difference
from eng e
inner join mkt m
on e.rnk = m.rnk