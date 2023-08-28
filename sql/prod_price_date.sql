WITH desc_prod AS (
  SELECT  product_id,
       new_price AS price,
       RANK()OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rk
  FROM Products 
  WHERE change_date <= ' 2019-08-16'
) 
SELECT DISTINCT p.product_id,
                COALESCE(d.price, 10) AS price
FROM Products AS p
LEFT JOIN desc_prod AS d
ON p.product_id = d.product_id AND d.rk = 1
