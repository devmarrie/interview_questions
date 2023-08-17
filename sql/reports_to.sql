
SELECT s.employee_id,
       s.name,
       COUNT(q.reports_to) AS reports_count,
       ROUND(AVG(q.age)) AS average_age
FROM Employees AS s
LEFT JOIN Employees AS q
ON s.employee_id = q.reports_to
GROUP BY s.employee_id
HAVING COUNT(q.reports_to) > 0
ORDER BY s.employee_id;