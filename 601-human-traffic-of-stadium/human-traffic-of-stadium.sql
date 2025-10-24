with cte1 as (select *, id - row_number() over (order by id) as grp
from stadium where people >= 100),

cte2 as (select *, count(grp) over (partition by grp) as ranking from cte1)

select id, visit_date, people from cte2 where ranking >= 3
order by visit_date