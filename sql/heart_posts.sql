-- Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.
-- Tables: facebook_reactions, facebook_posts

-- poster:int
-- friend:int
-- reaction:varchar
-- date_day:int
-- post_id:int

-- facebook_posts
-- post_id:int
-- poster:int
-- post_text:varchar
-- post_keywords:varchar
-- post_date:datetime

select distinct p.post_id, p.poster, p.post_text, p.post_keywords, p.post_date
from facebook_reactions r
right join facebook_posts p
on r. post_id = p.post_id
where r.reaction = 'heart';