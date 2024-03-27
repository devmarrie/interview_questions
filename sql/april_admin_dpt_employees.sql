-- Find the number of employees working in the Admin department that joined in April or later.
-- Table: worker

select count(*) as n_admins from worker
where month(joining_date) >= 4 and department = 'Admin';