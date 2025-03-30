/* 2025-03-30 15:02:56 [7 ms] */ 
show tables;
/* 2025-03-30 15:03:47 [3 ms] */ 
select * from budget LIMIT 100;
/* 2025-03-30 15:03:55 [1 ms] */ 
select * from budget ORDER BY `category` desc LIMIT 100;
/* 2025-03-30 15:04:57 [7 ms] */ 
describe budget;
/* 2025-03-30 15:12:35 [11 ms] */ 
describe expenses;
/* 2025-03-30 15:36:15 [4 ms] */ 
show tables;
/* 2025-03-30 15:48:09 [1 ms] */ 
SELECT * FROM budget LIMIT 100;
/* 2025-03-30 15:48:36 [1 ms] */ 
SELECT * FROM expenses LIMIT 100;
/* 2025-03-30 15:48:42 [1 ms] */ 
SELECT * FROM budget LIMIT 100;
/* 2025-03-30 15:48:45 [1 ms] */ 
SELECT * FROM customers LIMIT 100;
/* 2025-03-30 15:48:48 [1 ms] */ 
SELECT * FROM expenses LIMIT 100;
/* 2025-03-30 15:49:18 [1 ms] */ 
SELECT * FROM customers LIMIT 100;
/* 2025-03-30 15:49:21 [1 ms] */ 
SELECT * FROM budget LIMIT 100;
/* 2025-03-30 15:49:24 [1 ms] */ 
SELECT * FROM customers LIMIT 100;
/* 2025-03-30 15:49:30 [1 ms] */ 
SELECT * FROM expenses LIMIT 100;
/* 2025-03-30 15:49:33 [1 ms] */ 
SELECT * FROM budget LIMIT 100;
/* 2025-03-30 15:49:36 [1 ms] */ 
SELECT * FROM customers LIMIT 100;
/* 2025-03-30 15:52:47 [40 ms] */ 
insert customers(id, name, email, balance, created_at)
values (1, "Charles Feyi", 'olugbeng278@gmail.com', 220, '2025-01-10' );
/* 2025-03-30 15:52:48 [1 ms] */ 
SELECT * FROM customers LIMIT 100;
/* 2025-03-30 16:03:36 [8 ms] */ 
SELECT * from bank_db.customers where balance = '220' LIMIT 100;
/* 2025-03-30 16:51:57 [2 ms] */ 
SELECT * FROM expenses LIMIT 100;
