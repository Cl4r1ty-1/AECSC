import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute("""
        CREATE TABLE IF NOT EXISTS students_info (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          Name TEXT NOT NULL,
          Age INTEGER,
          Grade TEXT
          )
          """)

print("Success")