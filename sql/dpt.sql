WITH yes AS (
  SELECT employee_id,
         department_id,
         primary_flag
  FROM Employee
  WHERE primary_flag = 'Y'
)
SELECT DISTINCT e1.employee_id,
                COALESCE(y.department_id, e1.department_id) AS department_id
FROM Employee AS e1
LEFT JOIN yes AS  y
ON e1.employee_id = y.employee_id
