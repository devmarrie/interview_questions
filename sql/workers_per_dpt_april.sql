-- Find the number of workers by department who joined in or after April.

-- Output the department name along with the corresponding number of workers.

-- Sort records based on the number of workers in descending order.
-- Table: worker

select department, count(first_name) as num_workers
from worker
where month(joining_date) >= 4
group by department
order by 2 desc;