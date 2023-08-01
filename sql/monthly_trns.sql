# Write your MySQL query statement below
WITH status AS (
  SELECT DATE_FORMAT(trans_date, '%Y-%m') AS app_date,
         COUNT(state) AS approved,
         SUM(amount) AS tapp
  FROM Transactions
  WHERE state = 'approved'
  GROUP BY DATE_FORMAT(trans_date, '%Y-%m'),country
)
SELECT DATE_FORMAT(t.trans_date, '%Y-%m') AS month,
       t.country,
       COUNT(*) AS trans_count,
       s.approved AS approved_count,
       SUM(t.amount) AS trans_total_amount,
       s.tapp AS approved_total_amount
FROM Transactions AS t
LEFT JOIN status AS s
ON DATE_FORMAT(t.trans_date, '%Y-%m') = s.app_date
GROUP BY DATE_FORMAT(t.trans_date, '%Y-%m'), t.country;