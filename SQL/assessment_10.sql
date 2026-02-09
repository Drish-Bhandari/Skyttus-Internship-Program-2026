CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    member_name VARCHAR(50) NOT NULL,
    join_date DATE NOT NULL,
    status VARCHAR(10) CHECK (status IN ('Active', 'Inactive'))
);
CREATE TABLE meals (
    meal_id SERIAL PRIMARY KEY,
    meal_name VARCHAR(20) NOT NULL,
    meal_time VARCHAR(20)
);
CREATE TABLE menu (
    menu_id SERIAL PRIMARY KEY,
    meal_id INT NOT NULL,
    menu_date DATE NOT NULL,
    items VARCHAR(200),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    meal_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    amount INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_mode VARCHAR(20),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


INSERT INTO members (member_name, join_date, status) VALUES
('Amit',  '2025-10-01', 'Active'),
('Neha',  '2025-10-05', 'Active'),
('Rahul', '2025-11-01', 'Active'),
('Pooja', '2025-11-15', 'Inactive'),
('Karan', '2025-12-01', 'Active'),
('Jay',   '2025-12-10', 'Active');

INSERT INTO meals (meal_name, meal_time) VALUES
('Breakfast', '08:00 AM'),
('Lunch',     '01:00 PM'),
('Dinner',    '08:00 PM');

INSERT INTO menu (meal_id, menu_date, items) VALUES
(1, '2025-11-10', 'Poha, Tea'),
(2, '2025-11-10', 'Rice, Dal'),
(3, '2025-11-10', 'Roti, Sabji'),

(1, '2025-12-15', 'Idli, Sambar'),
(2, '2025-12-15', 'Veg Biryani'),
(3, '2025-12-15', 'Paneer Curry'),

(1, '2026-01-10', 'Upma, Coffee'),
(2, '2026-01-10', 'Rice, Rajma'),
(3, '2026-01-10', 'Chapati, Mix Veg');

INSERT INTO attendance (member_id, meal_id, attendance_date) VALUES
-- November
(1, 1, '2025-11-10'),
(1, 2, '2025-11-10'),
(2, 2, '2025-11-10'),
(3, 3, '2025-11-10'),

-- December
(1, 1, '2025-12-15'),
(3, 2, '2025-12-15'),
(5, 3, '2025-12-15'),
(6, 2, '2025-12-15'),

-- January
(1, 2, '2026-01-10'),
(2, 3, '2026-01-10'),
(5, 1, '2026-01-10'),
(6, 3, '2026-01-10');

INSERT INTO payments (member_id, amount, payment_date, payment_mode) VALUES
(1, 3000, '2025-11-05', 'Online'),
(2, 3000, '2025-11-06', 'Cash'),
(3, 2500, '2025-12-05', 'Online'),
(1, 3000, '2025-12-05', 'Online'),
(5, 3000, '2026-01-05', 'Cash');



-- List all Active Members
SELECT member_id, member_name, join_date
FROM members
WHERE status = 'Active'
ORDER BY join_date;

-- List all Inactive Members
SELECT member_id, member_name, join_date
FROM members
WHERE status = 'Inactive';

-- Members Who Joined in a Specific Month
SELECT member_id, member_name, join_date
FROM members
WHERE DATE_TRUNC('month', join_date) = DATE '2025-12-01';

-- Members Who Never Took Any Meal
SELECT m.member_id, m.member_name
FROM members m
LEFT JOIN attendance a
ON m.member_id = a.member_id
WHERE a.member_id IS NULL;

-- Total Attendance per Day
SELECT 
    attendance_date,
    COUNT(*) AS total_attendance
FROM attendance
GROUP BY attendance_date
ORDER BY attendance_date;

-- Meal-Wise Attendance Count
SELECT 
    m.meal_name,
    COUNT(a.attendance_id) AS meal_count
FROM attendance a
JOIN meals m
ON a.meal_id = m.meal_id
GROUP BY m.meal_name;

-- Member-Wise Total Meals Taken
SELECT 
    m.member_id,
    m.member_name,
    COUNT(a.attendance_id) AS total_meals
FROM members m
JOIN attendance a
ON m.member_id = a.member_id
GROUP BY m.member_id, m.member_name
ORDER BY total_meals DESC;

-- Members Who Missed Meals on a Given Date
SELECT m.member_id, m.member_name
FROM members m
WHERE m.member_id NOT IN (
    SELECT member_id
    FROM attendance
    WHERE attendance_date = '2026-01-10'
);

-- Most Consumed Meal
SELECT meal_name, meal_count
FROM (
    SELECT 
        m.meal_name,
        COUNT(*) AS meal_count,
        RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM attendance a
    JOIN meals m
    ON a.meal_id = m.meal_id
    GROUP BY m.meal_name
) t
WHERE rnk = 1;

-- Total Collection per Month
SELECT 
    DATE_TRUNC('month', payment_date) AS month,
    SUM(amount) AS total_collection
FROM payments
GROUP BY DATE_TRUNC('month', payment_date)
ORDER BY month;

-- Member-Wise Total Payment
SELECT 
    m.member_id,
    m.member_name,
    COALESCE(SUM(p.amount), 0) AS total_paid
FROM members m
LEFT JOIN payments p
ON m.member_id = p.member_id
GROUP BY m.member_id, m.member_name
ORDER BY total_paid DESC;

-- Members Who Have Not Made Any Payment
SELECT m.member_id, m.member_name
FROM members m
LEFT JOIN payments p
ON m.member_id = p.member_id
WHERE p.member_id IS NULL;

-- Members with Payments Below a Certain Amount
SELECT 
    m.member_id,
    m.member_name,
    SUM(p.amount) AS total_paid
FROM members m
JOIN payments p
ON m.member_id = p.member_id
GROUP BY m.member_id, m.member_name
HAVING SUM(p.amount) < 3000;

--Month-Wise Attendance Count
SELECT 
    DATE_TRUNC('month', attendance_date) AS month,
    COUNT(*) AS total_attendance
FROM attendance
GROUP BY DATE_TRUNC('month', attendance_date)
ORDER BY month;

-- Month-Wise Revenue Summary
SELECT 
    DATE_TRUNC('month', payment_date) AS month,
    SUM(amount) AS total_revenue
FROM payments
GROUP BY DATE_TRUNC('month', payment_date)
ORDER BY month;



-- Optimize at least 3 queries

-- 1. Members Who Never Took Any Meal
-- Why it can be slow :
-- attendance grows fast
-- member_id is frequently used in JOIN

-- Optimization by  creating Index
CREATE INDEX idx_attendance_member_id
ON attendance(member_id);

-- 2. Meal-Wise Attendance Count:
-- Why it can be slow
-- Aggregation on large attendance table
-- Frequent JOIN on meal_id

-- Optimization by creating Index
CREATE INDEX idx_attendance_meal_id
ON attendance(meal_id);


-- 3.Month-Wise Attendance Count
-- Why it can be slow
-- Date-based grouping
-- Full scan needed if no index

-- Optimization by creating Index
CREATE INDEX idx_attendance_date
ON attendance(attendance_date);
