-- Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews. Order by total reviews in descending order.
-- Table: yelp_business
-- First 5 rows of Expected Output:
-- category	review_cnt
-- Automotive	32
-- Auto Detailing	4
-- Restaurants	1703
-- Event Planning & Services	162
-- Food Delivery Services	30
SELECT
  TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(categories, ';', n), ';', -1)) AS category,
  SUM(review_count) AS review_cnt
FROM
  yelp_business
JOIN (
  SELECT 1 AS n UNION ALL
  SELECT 2 UNION ALL
  SELECT 3 UNION ALL
  SELECT 4 UNION ALL
  SELECT 5 UNION ALL
  SELECT 6 UNION ALL
  SELECT 7 UNION ALL
  SELECT 8 UNION ALL
  SELECT 9 UNION ALL
  SELECT 10
) AS numbers
ON
  CHAR_LENGTH(categories) - CHAR_LENGTH(REPLACE(categories, ';', '')) >= n - 1
GROUP BY
  category
ORDER BY
  review_cnt DESC;