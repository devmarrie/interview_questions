-- Calculate each user's average session time. 
-- A session is defined as the time difference between a page_load and page_exit. For simplicity, 
-- assume a user has only 1 session per day and if there are multiple of the same events on that day, 
-- consider only the latest page_load and earliest page_exit, with an obvious restriction that load 
-- time event should happen before exit time event . 
-- Output the user_id and their average session time.
-- Table:
-- facebook_web_log
-- user_id	timestamp	action
-- 0	2019-04-25 13:30:15	page_load
-- 0	2019-04-25 13:30:18	page_load
-- 0	2019-04-25 13:30:40	scroll_down
-- 0	2019-04-25 13:30:45	scroll_up
-- 0	2019-04-25 13:31:10	scroll_down
-- 0	2019-04-25 13:31:25	scroll_down
-- 0	2019-04-25 13:31:40	page_exit
-- 1	2019-04-25 13:40:00	page_load
-- 1	2019-04-25 13:40:10	scroll_down
-- 1	2019-04-25 13:40:15	scroll_down
-- 1	2019-04-25 13:40:20	scroll_down
-- 1	2019-04-25 13:40:25	scroll_down
-- 1	2019-04-25 13:40:30	scroll_down
-- 1	2019-04-25 13:40:35	page_exit
-- 2	2019-04-25 13:41:21	page_load
-- 2	2019-04-25 13:41:30	scroll_down
-- 2	2019-04-25 13:41:35	scroll_down
-- 2	2019-04-25 13:41:40	scroll_up
-- 1	2019-04-26 11:15:00	page_load
-- 1	2019-04-26 11:15:10	scroll_down
-- 1	2019-04-26 11:15:20	scroll_down
-- 1	2019-04-26 11:15:25	scroll_up
-- 1	2019-04-26 11:15:35	page_exit
-- 0	2019-04-28 14:30:15	page_load
-- 0	2019-04-28 14:30:10	page_load
-- 0	2019-04-28 13:30:40	scroll_down
-- 0	2019-04-28 15:31:40	page_exit
-- user_id:
-- Expected output:
-- user_id	avg
-- 0	1883.5
-- 1	35

with cte as (
select user_id, max(timestamp) as loaded, action,
    extract(day from timestamp) AS day
from facebook_web_log 
where action = 'page_load' 
group by extract(day from timestamp), user_id, action
),
ext_cte as (
select user_id, min(timestamp) as exited, action,
    extract(day from timestamp) AS day
from facebook_web_log 
where action = 'page_exit'
group by extract(day from timestamp), user_id, action
)
select l.user_id , AVG(e.exited - l.loaded) as avg
from cte l
inner join ext_cte e
on l.user_id = e.user_id and l.day = e.day
group by l.user_id;