WITH coun AS (
  SELECT teacher_id,
       subject_id,
       COUNT(*) AS c
  FROM Teacher
  GROUP BY subject_id, teacher_id
)
SELECT teacher_id,
       COUNT(*) AS cnt
FROM coun
GROUP BY teacher_id