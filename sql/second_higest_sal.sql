WITH ord AS (
SELECT id,
       salary,
       DENSE_RANK()OVER(ORDER BY salary DESC) AS rnk
FROM Employee
)

SELECT IFNULL((SELECT salary FROM ord WHERE rnk = 2 LIMIT 1), NULL) AS SecondHighestSalary
