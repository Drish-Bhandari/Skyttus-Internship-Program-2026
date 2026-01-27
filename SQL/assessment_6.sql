create table account(
	account_id int primary key,
	account_holder_name varchar(30) not null,
	balance decimal(10,2) 
)
insert into account
values
(1, 'Amit', 5000),
(2, 'Neha', 3000)

select * from account



-- Start a transaction 
-- Insert record into accounts 
-- Rollback changes 
begin;
insert into account 
values (3, 'Jay', 6000);
rollback;


-- Commit valid transactions
begin;
insert into account 
values (3, 'Jay', 6000);
commit;


-- Demonstrate transfer of money using transaction
begin;

-- debit from amit
update account
set balance = balance - 1000
where account_id = 1;

-- credit to neha 
update account
set balance = balance + 1000
where account_id = 2;

commit;

