select e.reports_to as employee_id, m.name, count(e.employee_id) as reports_count, round(avg(e.age)) as average_age
from employees e
join employees m on e.reports_to = m.employee_id
group by e.reports_to, m.name
order by e.reports_to