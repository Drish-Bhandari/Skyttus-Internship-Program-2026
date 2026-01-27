-- Create users table with: 
-- Primary key 
-- Unique email 
-- Not null password 
-- Add foreign key between orders and users 
-- Create index on email column 
-- Create view to display user order summary 


create table users(
	user_id int primary key,
	email varchar(50) unique,
	password varchar(20) not null
)

create table orders(
	order_id serial primary key,
	user_id int references users(user_id),
	order_date date,
	quantity int
);

-- Create index on email column 
create index idx_user_email
on users(email);

-- Create view to display user order summary 
create view user_order_summary as
select u.user_id, u.email, count(o.order_id) as total_orders, coalesce(SUM(o.quantity), 0) AS total_quantity
from users u
left join orders o
on u.user_id = o.user_id
group by u.user_id, u.email;

select * from user_order_summary




