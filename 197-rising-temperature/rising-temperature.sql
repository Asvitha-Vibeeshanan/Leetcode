select id 
from(
    select id,
    recordDate,
    temperature,
    lag(temperature) over (order by recordDate) as prev_temp,
    lag(recordDate) over(order by recordDate) as prev_date
    from Weather
) as temp_diff
where datediff(recordDate, prev_date) = 1
and temperature > prev_temp