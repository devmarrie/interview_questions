-- Table: Transactions

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | country       | varchar |
-- | state         | enum    |
-- | amount        | int     |
-- | trans_date    | date    |
-- +---------------+---------+
-- id is the primary key of this table.
-- The table has information about incoming transactions.
-- The state column is an enum of type ["approved", "declined"].

 

-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Transactions table:
-- +------+---------+----------+--------+------------+
-- | id   | country | state    | amount | trans_date |
-- +------+---------+----------+--------+------------+
-- | 121  | US      | approved | 1000   | 2018-12-18 |
-- | 122  | US      | declined | 2000   | 2018-12-19 |
-- | 123  | US      | approved | 2000   | 2019-01-01 |
-- | 124  | DE      | approved | 2000   | 2019-01-07 |
-- +------+---------+----------+--------+------------+
-- Output: 
-- +----------+---------+-------------+----------------+--------------------+-----------------------+
-- | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
-- +----------+---------+-------------+----------------+--------------------+-----------------------+
-- | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
-- | 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
-- | 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
-- +----------+---------+-------------+----------------+--------------------+-----------------------+


WITH status AS (
  SELECT DATE_FORMAT(trans_date, '%Y-%m') AS app_date,
         country,
         COUNT(state) AS approved,
         SUM(amount) AS tapp
  FROM Transactions
  WHERE state = 'approved'
  GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
)
SELECT DATE_FORMAT(t.trans_date, '%Y-%m') AS month,
       t.country,
       COUNT(*) AS trans_count,
       COALESCE(s.approved, 0) AS approved_count,
       SUM(t.amount) AS trans_total_amount,
       COALESCE(s.tapp, 0) AS approved_total_amount
FROM Transactions AS t
LEFT JOIN status AS s
ON DATE_FORMAT(t.trans_date, '%Y-%m') = s.app_date AND t.country = s.country
GROUP BY DATE_FORMAT(t.trans_date, '%Y-%m'), t.country;