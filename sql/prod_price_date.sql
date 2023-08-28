SELECT product_id, 
       COALESCE(MAX(CASE WHEN change_date <= "2019-08-16"
               THEN new_price END), 10) AS price
FROM Products
GROUP BY product_id