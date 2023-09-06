WITH sum_dates AS (
    SELECT visited_on,
        SUM(amount) AS tt
    FROM Customer
    GROUP BY visited_on
),
all_dates AS (
    SELECT visited_on,
        SUM(tt)OVER(
           ORDER BY visited_on
           ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(tt) OVER(
           ORDER BY visited_on
           ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount
    FROM sum_dates
    ORDER BY visited_on
)
SELECT visited_on,
       amount,
       average_amount
FROM all_dates
WHERE visited_on >= (
    SELECT DATE_ADD(visited_on, INTERVAL 6 DAY)
    FROM Customer 
    ORDER BY visited_on
    LIMIT 1 
)
ORDER BY visited_on;