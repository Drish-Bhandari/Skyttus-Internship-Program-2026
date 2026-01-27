select * from employees
INSERT INTO
	EMPLOYEES
VALUES
	(108, 'Jay', 1, 30000)

-- Find employees earning more than average salary 
select emp_id, emp_name, salary
from employees
where salary > (
    select avg(salary)
    from employees);

-- Find department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1;

-- Display employee with second highest salary 
SELECT emp_name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (SELECT MAX(salary) FROM employees)
);

-- Display employees working in same department as "Amit"
select emp_name as employee 
from employees
where dept_id = (select dept_id from employees where emp_name = 'Amit')






