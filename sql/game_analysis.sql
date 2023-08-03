SELECT ROUND((COUNT (*) / (SELECT COUNT(*) FROM total)), 2) AS fraction
FROM total
WHERE s > 0; 