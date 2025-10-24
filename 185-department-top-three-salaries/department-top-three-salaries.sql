# Write your MySQL query statement below
with high_salary as (select d.name as Department, e.name as Employee, e.salary as Salary,
dense_rank() over (partition by d.name order by salary desc) as ranking
from employee e
inner join department d on e.departmentId = d.id)

select Department, Employee, Salary
from high_salary
where ranking <= 3
