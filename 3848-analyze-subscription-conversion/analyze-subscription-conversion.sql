# Write your MySQL query statement below
select user_id, round(sum(case when activity_type ='free_trial' then activity_duration else 0 end)/nullif(count(CASE WHEN activity_type = 'free_trial' THEN 1 END), 0), 2) as trial_avg_duration,
round(sum(case when activity_type ='paid' then activity_duration else 0 end)/nullif(count(CASE WHEN activity_type = 'paid' THEN 1 END), 0), 2) as paid_avg_duration
from UserActivity
where user_id in (select distinct user_id from UserActivity where activity_type = "free_trial") and user_id in (select distinct user_id from UserActivity where activity_type = "paid")
group by user_id
order by user_id