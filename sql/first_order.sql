# Write your MySQL query statement below
WITH first_orders AS (
    SELECT delivery_id,
           customer_id,
           order_date,
           customer_pref_delivery_date,
           MIN(order_date) AS first
    FROM Delivery
    GROUP BY customer_id
),
imm_sch AS (
       SELECT customer_id,
              order_date,
              customer_pref_delivery_date,
              (CASE WHEN order_date = customer_pref_delivery_date
              THEN 'immidiate'
              ELSE 'scheduled'
              END) AS status
       FROM first_orders
)
SELECT ROUND((SUM(CASE WHEN i.status = 'immidiate' THEN 1 ELSE 0 END) / COUNT(1)) * 100, 2) AS immediate_percentage
FROM imm_sch AS i
INNER JOIN first_orders AS f
ON i.order_date = f.first