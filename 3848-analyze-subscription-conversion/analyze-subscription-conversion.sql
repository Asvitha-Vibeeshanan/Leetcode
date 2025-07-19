# Write your MySQL query statement below
select user_id, 
round(sum(case when activity_type = 'free_trial' then activity_duration else 0 end)/ 
NULLIF(SUM(CASE WHEN activity_type = 'free_trial' THEN 1 ELSE 0 END), 0),2) 
 AS trial_avg_duration, 
round(sum(case when activity_type = 'paid' then activity_duration else 0 end)/ 
 NULLIF(SUM(CASE WHEN activity_type = 'paid' THEN 1 ELSE 0 END), 0),2)
 AS paid_avg_duration
FROM UserActivity
WHERE user_id IN (
    SELECT DISTINCT user_id
    FROM UserActivity
    WHERE activity_type = 'free_trial'
)
AND user_id IN (
    SELECT DISTINCT user_id
    FROM UserActivity
    WHERE activity_type = 'paid'
)
GROUP BY user_id
ORDER BY user_id;