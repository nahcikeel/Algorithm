SELECT sell_date, COUNT(DISTINCT product) as num_sold,  GROUP_CONCAT(DISTINCT product separator ',') as products
FROM Activities
GROUP BY sell_date
