WITH nums AS (
SELECT id,
       CASE WHEN id % 2 = 0
         THEN id - 1
       WHEN id % 2 = 1 AND id + 1 NOT IN (SELECT id FROM Seat)
         THEN id
       ELSE id + 1
       END AS new
FROM Seat
)
SELECT n.id, s.student
FROM nums n
INNER JOIN Seat s
ON n.new = s.id
ORDER BY n.id ASC
    