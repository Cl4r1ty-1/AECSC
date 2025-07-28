import sqlite3
import csv

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Books")
c.execute("DROP TABLE IF EXISTS Authors")
c.execute("DROP TABLE IF EXISTS Genres")
c.execute("DROP TABLE IF EXISTS Book_Genres")
c.execute("DROP TABLE IF EXISTS Borrowers")

c.execute("""
          CREATE TABLE Books (
            BookID INTEGER PRIMARY KEY,
            Title TEXT,
            AuthorID INTEGER,
            PublicationYear INTEGER,
            FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID)
          )
          """)

c.execute("""
          CREATE TABLE Authors (
            AuthorID INTEGER PRIMARY KEY,
            Name TEXT,
            BirthDate DATE
          )
          """)

c.execute("""
          CREATE TABLE Genres (
            GenreID INTEGER PRIMARY KEY,
            Name TEXT
          )
          """)

c.execute("""
          CREATE TABLE Book_Genres (
            BookID INTEGER,
            GenreID INTEGER,
            FOREIGN KEY (BookID) REFERENCES Books (BookID),
            FOREIGN KEY (GenreID) REFERENCES Genres (GenreID)
          )
          """)

c.execute("""
          CREATE TABLE Borrowers (
            BorrowerID INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
          )
          """)

with open('books.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Books (BookID, Title, AuthorID, PublicationYear) VALUES (?, ?, ?, ?)", (int(row[0]), row[1], int(row[2]), int(row[3])))

with open('authors.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Authors (AuthorID, Name, BirthDate) VALUES (?, ?, ?)", (int(row[0]), row[1], row[2]))

with open('genres.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Genres (GenreID, Name) VALUES (?, ?)", (int(row[0]), row[1]))

with open('book_genres.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Book_Genres (BookID, GenreID) VALUES (?, ?)", (int(row[0]), int(row[1])))

with open('borrowers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Borrowers (BorrowerID, Name, Email) VALUES (?, ?, ?)", (int(row[0]), row[1], row[2]))

conn.commit()

print("Data entry complete!")

# SELECT Querys
# get titles of books
print("\nBook Titles:")
c.execute("SELECT Title FROM Books")
for title in c.fetchall():
    print(title[0])

# get names of authors
print("\nAuthor Names:")
c.execute("SELECT Name FROM Authors")
for name in c.fetchall():
    print(name[0])

# get publication years of books
print("\nPublication year of books:")
c.execute("SELECT PublicationYear FROM Books")
for year in c.fetchall():
    print(year[0])

# get names of genres
print("\nGenres:")
c.execute("SELECT Name FROM Genres")
for name in c.fetchall():
    print(name[0])

# get names and emails of borrowers
print("\nNames and Emails of Borrowers")
c.execute("SELECT Name, Email FROM Borrowers")
for name, email in c.fetchall():
    print(f"{name}: {email}")

conn.close()