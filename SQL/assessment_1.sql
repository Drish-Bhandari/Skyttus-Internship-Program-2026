create table students(
student_id INT,
name VARCHAR(50),
department VARCHAR(30),
year INT,
marks INT
)
insert into students (student_id, name, department, year, marks) 
values(1,Drish,IT,2026,90),
(2,'Meet','CSE',2026,85),
(3,'Preet','CSE',2026,70),
(4,'Kirtan','IT',2026,80),
(5,'Raj','CSE',2026,60),
(6,'Jay','IT',2026,85);


-- Display all student records
select * from students

-- Display only name and department 
select name, department from students

-- Find students with marks greater than 75
select * from students
where marks > 75

-- Display students from CSE department
select * from students
where department = 'CSE'

-- Sort students by marks (descending)
select * from students
order by marks desc

--Display top 3 scorers
select * from students
order by marks desc
limit 3
