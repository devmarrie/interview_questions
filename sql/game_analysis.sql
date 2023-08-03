-- Table: Activity

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

 

-- Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Activity table:
-- +-----------+-----------+------------+--------------+
-- | player_id | device_id | event_date | games_played |
-- +-----------+-----------+------------+--------------+
-- | 1         | 2         | 2016-03-01 | 5            |
-- | 1         | 2         | 2016-03-02 | 6            |
-- | 2         | 3         | 2017-06-25 | 1            |
-- | 3         | 1         | 2016-03-02 | 0            |
-- | 3         | 4         | 2018-07-03 | 5            |
-- +-----------+-----------+------------+--------------+
-- Output: 
-- +-----------+
-- | fraction  |
-- +-----------+
-- | 0.33      |
-- +-----------+
-- Explanation: 
-- Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

WITH last_game AS (
  SELECT player_id,
         device_id,
         event_date,
         games_played,
         COALESCE(LEAD(event_date)OVER(PARTITION BY player_id), 0) AS last_play
  FROM Activity
  ORDER BY player_id ASC
),
last_date AS(
  SELECT player_id,
         event_date,
         last_play,
         (CASE WHEN DATE_ADD(event_date, INTERVAL 1 DAY) = last_play
         THEN 1 ELSE 0
         END) AS prev
  FROM last_game
),
total AS (
  SELECT player_id,
       SUM(prev) AS s
  FROM last_date
  GROUP BY player_id
)
SELECT ROUND((COUNT(*) / (SELECT COUNT(*) FROM total)), 2) AS fraction
FROM total
WHERE s > 0;


