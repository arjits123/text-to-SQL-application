import sqlite3

# connect to sqlite
connection = sqlite3.connect('student.db')

# create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

#Create table
table_info = """

CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(25) NOT NULL,
age INT NOT NULL,
grade INT NOT NULL
)

"""

cursor.execute(table_info)

# insert the records

insert_query = """
INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
"""

# Sample records to insert
records = [
    ("Arjit Sharma", 14, 'A'),
    ("Ria Walia", 15, "B"),
    ("Charlie", 13, 'C'),
    ("Daisy", 16, 'A'),
    ("Eve", 17, 'B'),
    ("Frank", 18, 'C'),
    ("Gina", 19, 'A'),
    ("Hannah", 20, 'B'),
    ("Ivan", 21, 'C'),
    ("Jenny", 22, 'A')
]

for rec in records:
    cursor.execute(insert_query, rec)

print("Records inserted successfully.")

data = cursor.execute('''SELECT * FROM students''')

for row in data:
    print(row)

# Close the connection 
connection.commit()
connection.close()