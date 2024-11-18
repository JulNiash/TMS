drop table if exists sales;
drop table if exists books;
drop table if exists authors;

create table authors (
    id SERIAL primary key,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

create table books (
    id SERIAL primary key,
    title VARCHAR(50),
    author_id INT,
    publication_year int,
    foreign key (author_id) references authors (id)
);

create table sales (
    id SERIAL primary key,
    book_id INT,
    quantity INT,
    foreign key (book_id) references books (id)
);

insert into authors (first_name, last_name)
values ('Lev', 'Tolstoy'), 
		('Alexander', 'Pushkin'), 
		('Nikolay', 'Gogol'),
		('Vladimir', 'Mayakovskiy');

insert  into books (title, author_id, publication_year)
values ('Anna Karenina', 1, 1873), 
		('Voina i mir', 1, 1867), 
		('Kaptains daughter', 2, 1836), 
		('Dubrovskiy', 2, 1841), 
		('Dead souls', 3, 1842), 
		('Shinel', 3, 1842);
insert into books (title, publication_year)
values ('Djanga with shadows', '2015');

	
insert  into sales (book_id, quantity)
values (1, 250000), 
		(2, 350000), 
		(3, 160000), 
		(4, 230000), 
		(6, 140000);
	
select authors.first_name, authors.last_name, books.title
from authors
inner join books
on authors.id = books.author_id;

select authors.first_name, authors.last_name, books.title
from authors
left join books
on authors.id = books.author_id;

select authors.first_name, authors.last_name, books.title
from authors
right join books
on authors.id = books.author_id;

select authors.first_name, authors.last_name, books.title, sales.quantity
from authors
inner join books on authors.id = books.author_id 
inner join sales on books.id = sales.book_id; 

select authors.first_name, authors.last_name, books.title, sales.quantity
from authors
left join books on authors.id = books.author_id 
left join sales on books.id = sales.book_id;

select authors.first_name, authors.last_name, SUM(sales.quantity) AS total_quantity
from authors
inner join books on authors.id = books.author_id 
inner join sales on books.id = sales.book_id
group by authors.first_name, authors.last_name;

select authors.first_name, authors.last_name, SUM(sales.quantity) AS total_quantity
from authors
left join books on authors.id = books.author_id 
left join sales on books.id = sales.book_id
group by authors.first_name, authors.last_name;

select authors.first_name, authors.last_name, SUM(sales.quantity) AS total_quantity
from authors
inner join books on authors.id = books.author_id 
inner join sales on books.id = sales.book_id
group by authors.first_name, authors.last_name
order by total_quantity DESC
limit 1;

select books.title, authors.first_name, authors.last_name, SUM(sales.quantity) AS total_quantity
from books
inner join authors on books.author_id = authors.id
inner join sales on books.id = sales.book_id
group by books.title, authors.first_name, authors.last_name
having 
    SUM(sales.quantity) > (
        select 
            AVG(total_sales)
        from (
            select 
                SUM(sales.quantity) as total_sales
            from 
                sales
            inner join 
                books on sales.book_id = books.id
            group by 
                books.id
        ) as average_sales
    );