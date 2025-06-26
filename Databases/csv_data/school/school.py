import sqlite3
import csv

conn = sqlite3.connect("school.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Enrolments")
c.execute("""
        CREATE TABLE Enrolments (
          StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
          FirstName TEXT,
          LastName TEXT,
          Course TEXT,
          StartDate DATE,
          FeesPaid REAL
          )
          """)

with open('enrolments_100.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        c.execute("""
        INSERT INTO Enrolments (FirstName, LastName, Course, StartDate, FeesPaid)
        VALUES (?, ?, ?, ?, ?)
                  """, (row[0], row[1], row[2], row[3], float(row[4])))
        
conn.commit()
conn.close()

print("You did it bruh check sqlite now")