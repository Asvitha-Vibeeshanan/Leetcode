# Write your MySQL query statement below
select name as Customers
from Customers
left join Orders on Customers.id = orders.customerID
where orders.customerID is null