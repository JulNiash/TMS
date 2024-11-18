create table employees (
	id serial primary key,
	name varchar(255) not null unique,
	position varchar(255) not null,
	department varchar(255),
	salary int 
);

INSERT INTO employees (name, position, department, salary)
VALUES ('Ilya Kuleshov', 'seller', 'sales', 1500.00),
		('Bogdan Bazaka', 'intern', 'sales', 300.00),
		('Darya Morghauchuk', 'main seller', 'sales', 4500.00),
		('Vadim Juk', 'Manager', 'sales', 7000.00),
		('VLadimir Lenin', 'seller', 'sales', 1350.00);

update employees
set salary = 5000
where name = 'Ilya Kuleshov';

alter table employees
add column HireDate DATE;

update employees
set HireDate = CURRENT_DATE - (RANDOM() * INTERVAL '10 years');

select name, salary from employees
where salary >= 5000;

select name, department from employees
where department = 'sales';

SELECT AVG(salary) AS average_salary
FROM employees;

drop table employees