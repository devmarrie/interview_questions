SELECT DISTINCT e1.employee_id,
                COALESCE(e2.department_id, e1.department_id) AS department_id
FROM Employee AS e1
LEFT JOIN Employee AS e2
ON e1.employee_id = e2.employee_id AND e2.primary_flag = 'y'
