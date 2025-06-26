import sqlite3
import csv

conn = sqlite3.connect("retail.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Orders")
c.execute("""
        CREATE TABLE Orders (
          OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
          CustomerName TEXT,
          Product TEXT,
          Quantity INTEGER,
          OrderDate DATE,
          TotalAmount REAL
          )
          """)

with open('orders_100.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        c.execute("""
        INSERT INTO Orders (CustomerName, Product, Quantity, OrderDate, TotalAmount)
        VALUES (?, ?, ?, ?, ?)
                  """, (row[0], row[1], int(row[2],), row[3], float(row[4])))
        
conn.commit()
conn.close()

print("You did it bruh check sqlite now")