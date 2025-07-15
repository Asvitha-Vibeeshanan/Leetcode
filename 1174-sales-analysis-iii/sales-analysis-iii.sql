# Write your MySQL query statement below
select p.product_id, p.product_name 
from Product p
where p.product_id in (
    select s.product_id 
    from sales s 
    group by product_id
    having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31')