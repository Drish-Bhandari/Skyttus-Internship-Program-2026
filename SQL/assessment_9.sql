create table employee (
    emp_id int,
    emp_name varchar(50),
    salary int,
    hire_date date
);

insert into employee values
(1, 'amit', 50000, '2025-09-15'),
(2, 'neha', 60000, '2025-11-10'),
(3, 'rahul', 55000, '2025-08-01'),
(4, 'pooja', 60000, '2026-01-05'),
(5, 'karan', 45000, '2025-12-20'),
(6, 'amit', 50000, '2025-09-15'),
(7, 'jay', 50000, '2025-09-21');

update employee 
set salary = 50000 
where emp_id = 5

-- Write query to find Nth highest salary
-- 3rd highest salary
select distinct salary
from employee
order by salary desc
offset 3-1
limit 1

-- Remove duplicate records
delete from employee
where emp_id not in (select min(emp_id) from employee
    group by emp_name, salary, hire_date
);

select * from employee

-- Find continuous duplicate values
select emp_id, emp_name, salary
from (select *, lag(salary) over (order by emp_id) as prev_salary
    from employee) t
where salary = prev_salary;









