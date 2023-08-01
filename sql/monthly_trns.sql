# Write your MySQL query statement below
WITH status AS (
  SELECT trans_date,
         COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved,
         SUM(CASE WHEN state = 'approved' THEN amount END) AS tapp
  FROM Transactions
  # WHERE state = 'approved'
  GROUP BY trans_date,country
)
SELECT DATE_FORMAT(t.trans_date, '%Y-%m') AS month,
       t.country,
       COUNT(*) AS trans_count,
       s.approved AS approved_count,
       SUM(amount) AS trans_total_amount,
       s.tapp AS approved_total_amount
FROM Transactions AS t
LEFT JOIN status AS s
ON t.trans_date = s.trans_date
GROUP BY DATE_FORMAT(t.trans_date, '%Y-%m'), t.country;