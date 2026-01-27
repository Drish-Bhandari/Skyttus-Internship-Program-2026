create table customers (
    customer_id int primary key,
    name varchar(50),
    city varchar(50)
);
create table products (
    product_id int primary key,
    product_name varchar(50),
    price int
);
create table orders (
    order_id int primary key,
    customer_id int references customers(customer_id),
    order_date date,
    amount int
);
create table order_items (
    order_id int references orders(order_id),
    product_id int references products(product_id),
    quantity int,
    primary key (order_id, product_id)
);

insert into customers values
(1, 'Amit', 'Mumbai'),
(2, 'Neha', 'Delhi'),
(3, 'Rahul', 'Pune'),
(4,'Jay','Ahmedabad');

insert into products values
(101, 'laptop', 50000),
(102, 'mouse', 500),
(103, 'keyboard', 1500);

insert into orders values
(1001, 1, '2026-01-10', 51500),
(1002, 2, '2026-01-12', 500),
(1003, 3, '2026-01-15', 1500);
(1004, 1, '2026-01-16', 1500),
(1005, 3, '2026-01-17', 1600);

insert into order_items values
(1001, 101, 1),
(1001, 102, 1),
(1002, 102, 2),
(1003, 103, 1),
(1004, 103, 3),
(1005, 103, 2);

select * from customers
select * from products
select * from orders
select * from order_items

-- Total orders per customer 
select c.name, count(o.order_id) as total_order
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.name 

-- Customers who never placed an order
select c.name
from customers c
left join orders o on c.customer_id = o.customer_id
where o.order_id is null 

-- Highest selling product 
select p.product_name as higest_selling_product, sum(oi.quantity) as total_quantity_sold
from products p
join order_items oi on p.product_id = oi.product_id
group by p.product_id, p.product_name
order by total_quantity_sold desc
limit 1;

-- Monthly sales report 
select to_char(o.order_date, 'yyyy-mm') as month, sum(oi.quantity * p.price) as total_sales
from orders o
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id
group by to_char(o.order_date, 'yyyy-mm')
order by month;

-- customers with total purchase > ₹50,000 
select c.customer_id, c.name, sum(oi.quantity * p.price) as total_purchase
from customers c
join orders o
on c.customer_id = o.customer_id
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id
group by c.customer_id, c.name
having sum(oi.quantity * p.price) > 50000;

--Top 3 cities by revenue
select c.city, sum(oi.quantity * p.price) as total_revenue
from customers c
join orders o
on c.customer_id = o.customer_id
join order_items oi
on o.order_id = oi.order_id
join products p
on oi.product_id = p.product_id
group by c.city
order by total_revenue desc
limit 3;





