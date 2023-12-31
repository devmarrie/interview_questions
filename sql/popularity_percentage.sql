-- Find the popularity percentage for each user on Meta/Facebook. 
-- The popularity percentage is defined as the total number of friends the user has divided by the 
-- total number of users on the platform, then converted into a percentage by multiplying by 100.

-- Output each user along with their popularity percentage. Order records in ascending order by user id.

-- The 'user1' and 'user2' column are pairs of friends.
-- Table: facebook_friends                                                                                                                        
-- user1	user2
-- 2	      1
-- 1	         3
-- 4	     1
-- 1	         5
-- 1	         6
-- 2	     6
-- 7	         2
-- 8	     3
-- 3	     9   

-- expected output of the first five columns                                                                                                                                                                                         user1	popularity_percent
-- 1	             55.556
-- 2	         33.333
-- 3	         33.333
-- 4	         11.111
-- 5	         11.111

with usr_pop AS (
SELECT user1 AS user_id, user2 AS friend_id FROM facebook_friends
UNION
SELECT user2 AS user_id, user1 AS friend_id FROM facebook_friends
)
SELECT user_id as user1, 
    (
    COUNT( DISTINCT friend_id) / (
    SELECT COUNT(DISTINCT user_id) AS tt
    FROM usr_pop
    ) ) *100 as popularity_percent
FROM usr_pop
GROUP BY user_id
ORDER BY user_id
