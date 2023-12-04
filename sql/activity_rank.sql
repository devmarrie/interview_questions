-- Find the email activity rank for each user. 
-- Email activity rank is defined by the total number of emails sent. 
-- The user with the highest number of emails sent will have a rank of 1, and so on. 
-- Output the user, total emails, and their activity rank. 
-- Order records by the total emails in descending order. 
-- Sort users with the same number of emails in alphabetical order.
-- In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. 
-- For tie breaker use alphabetical order of the user usernames.
-- Table example:
-- id	from_user	to_user	day
-- 0	6edf0be4b2267df1fa	75d295377a46f83236	10
-- 1	6edf0be4b2267df1fa	32ded68d89443e808	6
-- 2	6edf0be4b2267df1fa	55e60cfcc9dc49c17e	10
-- 3	6edf0be4b2267df1fa	e0e0defbb9ec47f6f7	6
-- 4	6edf0be4b2267df1fa	47be2887786891367e	1

-- Expected output
-- from_user	total_emails	row_number
-- 32ded68d89443e808	19	1
-- ef5fe98c6b9f313075	19	2
-- 5b8754928306a18b68	18	3
-- 55e60cfcc9dc49c17e	16	4
-- 91f59516cb9dee1e88	16	5

with cte AS (
select from_user, COUNT(*) AS total_emails
from google_gmail_emails
group by from_user
)
select from_user, total_emails,
    row_number() over(order by total_emails DESC,from_user) as row_number
from cte 
order by total_emails DESC, from_user
;