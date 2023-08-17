WITH emp AS (
  SELECT reports_to,
       COUNT(*) AS reports_count,
       ROUND(AVG(age)) AS average_age
  FROM Employees
  WHERE reports_to IS NOT NULL
  GROUP BY reports_to
)
SELECT s.employee_id,
       s.name,
       q.reports_count,
       q.average_age
FROM Employees AS s
LEFT JOIN emp AS q
ON s.employee_id = q.reports_to
WHERE s.reports_to is null;