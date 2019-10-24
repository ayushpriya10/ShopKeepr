import sqlite3

conn = sqlite3.connect('packages.db')

print("Created and Connected to Database Successfully")

conn.execute(
    '''CREATE TABLE PACKAGES (PID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,VERSION TEXT, PARENTID INT DEFAULT NULL 
    );''')

print("Table Created Successfully")

conn.close()
