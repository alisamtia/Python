# Limit,Orderby,Like


# Limit
# Show the tables by limit
# SELECT * FROM STUDENTS LIMIT 5;


# SELECT * FROM students WHERE first_name LIKE "%nk%";
# Search with the length of text with sql
# we can use _
# SELECT * FROM students WHERE first_name LIKE "___";


# Order by:
# SELECT first_name FROM STUDENTS ORDER BY first_name;
# SELECT * FROM STUDENTS ORDER BY first_name;
# SELECT id,first_name,age FROM STUDENTS ORDER BY age,first_name;







# All letters will be in ascending
# If we want in decending we write
# SELECT first_name FROM STUDENTS ORDER BY first_name DESC;



INSERT INTO students(first_name,last_name,age) VALUES
('Ty', 'Ayelloribbin',12),
('Hugo', 'First',23),
('Percy', 'Vere',13),
('Jack', 'Aranda',14),
('Olive', 'Tree',23),
('Fran G.', 'Pani',21),
('John', 'Quil',52),
('Ev R.', 'Lasting',15),
('Anne', 'Thurium',17),
('Cherry', 'Blossom',19),
('Glad I.', 'Oli',17),
('Ginger', 'Plant',20),
('Del', 'Phineum',21),
('Rose', 'Bush',22),
('Perry', 'Scope',23),
('Frank N.', 'Stein',24),
('Roy L', 'Commishun',25),
('Pat', 'Thettick',26),
('Percy', 'Kewshun',27),
('Rod', 'Knee',29),
('Hank', 'R. Cheef',12);


