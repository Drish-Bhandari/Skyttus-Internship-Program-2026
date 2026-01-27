-- Count total number of students 
select * from students

select count(*) as total_student
from students

-- Find average marks of students
select avg(marks) as average_marks
from students

-- Find highest and lowest marks
select max(marks) as Higest_marks , min(marks) as Lowest_marks
from students

-- Find department-wise average marks 
select department, avg(marks) as average_marks
from students
group by department

-- Display departments where average marks > 70
select department, avg(marks) as average_marks
from students
group by department
having  avg(marks) > 70
