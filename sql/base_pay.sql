-- Find the base pay for Police Captains.
-- Output the employee name along with the corresponding base pay.
-- Table: sf_public_salaries

select employeename, basepay 
from sf_public_salaries
where jobtitle = 'CAPTAIN III (POLICE DEPARTMENT)';