SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b ON a.id + 1 = b.id AND a.num = b.num
JOIN Logs c ON a.id + 2 = c.id AND a.num = c.num;