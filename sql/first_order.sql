WITH full_tb AS (
       SELECT delivery_id,
              customer_id,
              order_date,
              customer_pref_delivery_date,
              MIN(order_date) OVER(PARTITION BY customer_id) AS first_date,
              (CASE WHEN order_date = customer_pref_delivery_date
                 THEN 'immediate'
                 ELSE 'scheduled'
                 END) AS status
       FROM Delivery
),
order_del AS (
       SELECT customer_id,
              delivery_id,
              first_date,
              status
       FROM full_tb
       WHERE first_date = order_date
)
SELECT ROUND((
       (
              SUM(CASE WHEN status = 'immediate' THEN 1 ELSE 0 END) / COUNT(*)
       ) * 100), 2) AS immediate_percentage
FROM order_del 