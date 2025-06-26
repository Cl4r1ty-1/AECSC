import sqlite3
import csv

conn = sqlite3.connect("movies.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Movies")
c.execute("""
        CREATE TABLE Movies (
          MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
          Title TEXT NOT NULL,
          Genre TEXT,
          ReleaseYear INTEGER,
          BoxOffice REAL,
          IsSequel BOOLEAN
          )
          """)

# open csv file and insert data
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    #skip header row if your csv file has headers
    next(reader) # remove this line

    # loop and insert each row
    for row in reader:
        c.execute("""
        INSERT INTO Movies (Title, Genre, ReleaseYear, BoxOffice, IsSequel)
        VALUES (?, ?, ?, ?, ?)
                  """, (row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
        
# commit changes and close
conn.commit()
conn.close()

print("CSV data imported successfully into the Movies database")