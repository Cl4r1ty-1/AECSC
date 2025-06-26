import sqlite3

conn = sqlite3.connect("employees.db")
c = conn.cursor()

c.execute("""
        CREATE TABLE IF NOT EXISTS employees (
          Employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
          Name TEXT NOT NULL,
          Department TEXT,
          Salary REAL
          )
          """)

print("Success")