# How to take a primary key to a value
# CREATE TABLE insta_users(user_name VARCHAR(100) DEFAULT "UNKNOWN" NOT NULL PRIMARY KEY,password VARCHAR(100) DEFAULT -1 NOT NULL);
# CREATE TABLE emp(id INT PRIMARY KEY,name VARCHAR(100),sallary INT);
# CREATE TABLE emp(id INT,name VARCHAR(100),sallary INT,PRIMARY KEY(id));
# Primary key will not give any error


# How to make the auto increament to the id
# CREATE TABLE emp_new(id INT AUTO_INCREAMENT,name VARCHAR(100),sallary INT,PRIMARY KEY(id));
