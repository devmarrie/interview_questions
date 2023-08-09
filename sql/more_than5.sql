WITH per AS (
  SELECT class, COUNT(*) AS c
  FROM Courses
  GROUP BY class
)
SELECT class
FROM per
WHERE c >= 5;