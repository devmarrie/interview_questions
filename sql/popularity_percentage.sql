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