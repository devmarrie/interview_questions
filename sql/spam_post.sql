-- Calculate the percentage of spam posts in all viewed posts by day. 
-- A post is considered a spam if a string "spam" is inside keywords of the post. 
-- Note that the facebook_posts table stores all posts posted by users. 
-- The facebook_post_views table is an action table denoting if a user has viewed a post.
-- Tables: 
-- facebook_posts
-- post_id:int
-- poster:int
-- post_text:varchar
-- post_keywords:varchar
-- post_date:datetime

-- facebook_post_views
-- post_id:int
-- viewer_id:int

-- Expected Output
-- post_date	spam_share
-- 2019-01-01	100
-- 2019-01-02	50

with wote as (
select p.post_date, count(v.viewer_id) as all_views
from facebook_posts p
inner join facebook_post_views v
on p.post_id = v.post_id
group by p.post_date
),
waspam as (
select p.post_date, count(v.viewer_id) as spam_views
from facebook_posts p
inner join facebook_post_views v
on p.post_id = v.post_id
where p.post_keywords like '%spam%'
group by p.post_date
)
select a.post_date,
    (b.spam_views / a.all_views) * 100 as spam_share
from wote a
inner join waspam b
on a.post_date = b.post_date


