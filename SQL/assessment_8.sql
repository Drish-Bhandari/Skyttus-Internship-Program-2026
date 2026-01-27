-- Add index to improve search on orders.customer_id
create index idx_orders_customer_id
on orders(customer_id);

-- Use EXPLAIN to analyze query
explain analyze
select * from orders
where customer_id = 1;


-- Optimize a slow join query
create index idx_customers_city
on customers(city);

select c.customer_id, c.name, o.order_id, o.amount
from customers c
join orders o
on c.customer_id = o.customer_id
where c.city = 'Mumbai';

explain analyze
select c.customer_id, c.name, o.order_id, o.amount
from customers c
join orders o
on c.customer_id = o.customer_id
where c.city = 'Mumbai';


-- Explain when index should not be used
-- function on indexed column (index ignored)

explain analyze
select *
from customers
where lower(city) = 'Mumbai';
