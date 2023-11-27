 # CREATE TABLE data(id INT AUTO_INCREMENT,first_name VARCHAR(100),last_name VARCHAR(100),PRIMARY KEY(id));

# INSERT INTO data(first_name,last_name) VALUES ('John','smith'),('William','brown'),('Gorege','Johnson'),('merry','brown'),('Joseph','smith'),('Ann','brown')

# How to read duplicate values in one tine we use distant
# SELECT DISTINCT last_name from data;



# Concate two strings:
# SELECT CONCAT(first_name,' ',last_name) FROM data AS full_name


# Add a new field
# ALTER TABLE data ADD s_email VARCHAR(100) DEFAULT 'UNKNOWN';

# Update all emails:
# SELECT CONCAT(first_name,last_name) from data AS full_name;ALTER TABLE data ADD s_email VARCHAR(100) DEFAULT 'UNKNOWN';


# Substring
# SELECT SUBSTRING('hELLO',1,2)
# SELECT * FROM data WHERE SUBSTRING(first_name,1,1) = 'A';