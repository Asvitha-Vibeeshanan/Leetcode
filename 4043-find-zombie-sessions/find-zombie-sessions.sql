# Write your MySQL query statement below
with cte1 as (
    select 
        session_id, 
        user_id, 
        TIMESTAMPDIFF(MINUTE, MAX(CASE WHEN event_type = 'app_open' THEN event_timestamp END),
                              MAX(CASE WHEN event_type = 'app_close' THEN event_timestamp END)
        ) AS session_duration_minutes, 
        sum(case when event_type = 'scroll' then 1 else 0 end) as scroll_count, 
        round(sum(case when event_type = 'click' then 1 else 0 end)/sum(case when event_type = 'scroll' then 1 else 0 end),2) as click_ratio,
        sum(case when event_type = 'purchase' then 1 else 0 end) as purchase_count  
from app_events
group by user_id)


select 
    session_id, 
    user_id, 
    session_duration_minutes, 
    scroll_count 
from cte1 
where 
    scroll_count >= 5 
    and click_ratio < 0.20 
    and session_duration_minutes > 30 
    and purchase_count = 0
order by scroll_count desc, session_id;