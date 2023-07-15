
-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

WITH prev AS (
  SELECT id,
         temperature,
         recordDate,
         LAG(temperature) OVER(ORDER BY recordDate) as yesterday
  FROM Weather
)
SELECT prev.id 
FROM prev
  INNER JOIN Weather
  ON prev.recordDate = DATE_ADD(Weather.recordDate, INTERVAL 1 DAY)
WHERE prev.temperature > prev.yesterday;
