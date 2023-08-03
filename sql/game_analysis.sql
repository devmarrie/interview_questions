# Write your MySQL query statement below
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


