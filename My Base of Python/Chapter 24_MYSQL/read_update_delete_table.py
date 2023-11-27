# Create Table books(book_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100) DEFAULT 'UNKNOWN',author VARCHAR(100) DEFAULT "UNKNOWN",price INT);
# INSERT INTO books(name,author,price) VALUES ('Think and Grow','Ali Clear',2000),('Power of now','James Clear',1000),('Automic Habits','James Now',500),("Rich DAD Poor dad","RObert",2000)



# How to selct a specific column
# SELECT name,price FROM books;

# Filter a value from any coulmn
# SELECT name FROM books WHERE author = 'Ali Clear';
# SELECT * FROM books WHERE author = 'Ali Clear';

# Price Filter
# SELECT * FROM books WHERE price<3000 = 'Ali Clear';

# Update Filter
# UPDATE books SET price=200 WHERE author='James Now';


# Update FIlter
# UPDATE books SET price=1000 WHERE book_id = 4;

# delete data
# Delte everythinf
# DELETE FROM books;

# DELETE FROM books WHERE price>=2000;

# select anything as anyother name
# select name as Book_Name, price from books;