# Write your MySQL query statement below
with cte as (select turn, person_id, person_name, weight, sum(weight) over (order by turn) as total_weight
from Queue)

select person_name from cte where total_weight <= 1000
order by total_weight desc limit 1

-- SELECT person_name from (select person_name,turn,
-- sum(weight) over (order by turn) as cum from queue) p1
-- where cum<=1000 order by turn desc limit 1;