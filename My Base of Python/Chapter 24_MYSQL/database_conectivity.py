# Install my sql conector
# pip install msql-connector-python


# Open command line client:
# See status there

import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='m3myname@ali',database='ali')# ,

# print(conn)
my_cursor=conn.cursor()

# query='CREATE DATABASE ali'
# query='SHOW DATABASES'
# query='USE ali; CREATE TABLE student(name VARCHAR(200),age INT)'
# query='INSERT INTO student(name,age) VALUE (%s,%s)'
# values=('Muhammad ali',12)

# query='INSERT INTO student(name,age) VALUES (%s,%s)'
# values=[('Muhammad ali',12),('Muhammad alian',11),('Uzma Shaheen',24),('Ahmed',10)]
# my_cursor.executemany(query,values)

query='SELECT * FROM student'

my_cursor.execute(query)

for i in my_cursor:
    print(i)

# for i in my_cursor:
#     print(i)

#Get a list of all databases
# print(my_cursor.fetchall())

conn.commit()
conn.close()