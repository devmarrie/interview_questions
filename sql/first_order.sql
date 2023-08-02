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
              (CASE WHEN first = customer_pref_delivery_date
              THEN 'immidiate'
              ELSE 'scheduled'
              END) AS status
       FROM first_orders
)
SELECT ROUND((COUNT(*) / (SELECT COUNT(1) FROM imm_sch)) * 100, 2) AS immediate_percentage
FROM imm_sch
WHERE status = 'immidiate'
GROUP BY status