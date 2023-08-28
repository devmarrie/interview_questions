SELECT DISTINCT p.product_id,
       COALESCE(CASE WHEN MAX(pr.change_date) THEN pr.new_price END , 10) AS price
FROM Products AS p
LEFT JOIN Products AS pr
ON p.product_id = pr.product_id AND pr.change_date <= ' 2019-08-16'
GROUP BY pr.product_id