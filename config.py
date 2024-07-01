# To work with mysql database

import mysql.connector

# Connect to mysql database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="library_management_system"
)

# Create a cursor
cursor = connection.cursor()

if cursor:
    print("Connected to database")
else:
    print("Not connected to database")
    
# Create a table
# cursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2))")

cursor.execute("SHOW TABLES")
cursor.execute("CREATE TABLE publisher (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), author VARCHAR(255))")

for table in cursor:
    print(table)
    
    
cursor.close()
connection.close()


# Insert a record
# cursor.execute("INSERT INTO products (name, price) VALUES ('Book', 10.99)")