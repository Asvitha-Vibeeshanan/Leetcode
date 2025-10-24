# Write your MySQL query statement below
with unique_records as (select *,
count(*) over (partition by lat, lon) as attempts,
count(*) over (partition by tiv_2015) as same_tivs
from Insurance)

select round(sum(tiv_2016), 2) as tiv_2016
from unique_records
where attempts = 1 and same_tivs > 1