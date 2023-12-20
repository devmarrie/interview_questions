-- Find the total number of downloads for paying and non-paying users by date. 
-- Include only records where non-paying customers have more downloads than paying customers. 
-- The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.
-- Tables: ms_user_dimension, ms_acc_dimension, ms_download_facts
-- Expected output
-- date	non_paying	paying
-- 2020-08-16	15	14
-- 2020-08-17	45	9
-- 2020-08-18	10	7
-- 2020-08-21	32	17

where n.non_paying > y.paying

with nos as (
select d.date, sum(d.downloads) as non_paying
from ms_user_dimension u
inner join ms_acc_dimension a
on u.acc_id = a.acc_id
inner join ms_download_facts d
on u.user_id = d.user_id
where a.paying_customer = 'no'
group by d.date
),
yeses as (
select d.date, sum(d.downloads) as paying
from ms_user_dimension u
inner join ms_acc_dimension a
on u.acc_id = a.acc_id
inner join ms_download_facts d
on u.user_id = d.user_id
where a.paying_customer = 'yes'
group by d.date
)
select n.date, n.non_paying, y.paying
from nos n
inner join yeses y
on n.date = y.date
where n.non_paying > y.paying
order by n.date;