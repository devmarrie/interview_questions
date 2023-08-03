# Write your MySQL query statement below
WITH last_game AS (
  SELECT player_id,
         device_id,
         event_date,
         games_played,
         COALESCE(LEAD(event_date)OVER(PARTITION BY device_id, player_id), 0) AS last_play
  FROM Activity
  ORDER BY player_id ASC
),
last_date AS(
  SELECT player_id,
        #  event_date,
        #  last_play,
         (CASE WHEN  last_play <> 0
         THEN 1 ELSE 0
         END) AS prev
  FROM last_game
  # WHERE last_play <> 0
  # GROUP BY player_id
)
# # total AS (
#   SELECT player_id,
#        COUNT(*) AS all
#   FROM last_game
#   GROUP BY player_id
# # )
SELECT ROUND((COUNT(*) / (SELECT COUNT(*) FROM last_date)), 2) AS fraction
FROM last_date
WHERE prev > 0;


