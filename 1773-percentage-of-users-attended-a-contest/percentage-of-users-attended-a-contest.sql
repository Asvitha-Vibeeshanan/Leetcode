# Write your MySQL query statement below
select 
    contest_id, 
    round(count(distinct user_id) * 100.00 /(select count(*) from Users), 2) as percentage
from register
group by contest_id
order by percentage desc, contest_id ASC;

-- SELECT 
--   r.contest_id,
--   ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
-- FROM Register r
-- GROUP BY r.contest_id
-- ORDER BY r.contest_id;