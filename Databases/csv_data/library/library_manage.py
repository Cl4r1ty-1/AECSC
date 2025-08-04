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

# WHERE Queries
# get books with publication year pver 2000
print("\nBooks older than 2000")
c.execute("SELECT * FROM Books WHERE PublicationYear > 2000")
for book in c.fetchall():
    print(book[0])

# get harper lee books
print("\nBooks written by Harper Lee")
c.execute("SELECT Title FROM Books WHERE AuthorID = 2")
for book in c.fetchall():
    print(book[0])

# Dystopian books
print("\nDystopian Books")
c.execute("SELECT * FROM Books WHERE BookID = (SELECT BookID FROM Book_Genres WHERE GenreID = 1)")
for book in c.fetchall():
    print(book)

# fetch authors born after 1900
print("\nAuthors born after 1900")
c.execute("SELECT * FROM Authors WHERE BirthDate > '1900-01-01'")
for author in c.fetchall():
    print(author)

# retreive borrowers with names starting with 'J'
print("\nBorrowers with names starting with 'J'")
c.execute("SELECT * FROM Borrowers WHERE Name LIKE 'J%'")
for borrower in c.fetchall():
    print(borrower)

# retrieve the titles and authors of all books where the author's birth year is after 1900.
print("\nBooks and authors where author's birth year is after 1900")
c.execute("""
        SELECT Books.Title, Authors.Name
        FROM Books
        INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID
        WHERE Authors.BirthDate > '1900-01-01'
          """)
for book, author in c.fetchall():
    print(f'{book} by {author}')

# retrieve titles and genres of all books where the genre is 'classic'
print("\nTitles and genres of all books where the genre is 'classic'")
c.execute("""
        SELECT Books.Title, Genres.Name
        FROM Books
        INNER JOIN Book_Genres ON Books.BookID = Book_Genres.BookID
        INNER JOIN Genres ON Book_Genres.GenreID = Genres.GenreID
        WHERE Genres.Name = 'Classic'
          """)
for book, genre in c.fetchall():
    print(f'{book} is a {genre}')

# fetch the titles, authors, and publication years of all books where the genre is "Classic" and the author's birth year is after 1900.
print("\nTitles, authors, and publication years of all books where the genre is 'Classic' and the author's birth year is after 1900")
c.execute("""
        SELECT Books.Title, Authors.Name, Books.PublicationYear
        FROM Books
        INNER JOIN Book_Genres ON Books.BookID = Book_Genres.BookID
        INNER JOIN Genres ON Book_Genres.GenreID = Genres.GenreID
        INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID
        WHERE Genres.Name = 'Classic' AND Authors.BirthDate > '1900-01-01'
          """)

for book, author, year in c.fetchall():
    print(f'{book} by {author} was published in {year}')

# retreive the title and authors of all books where the author was born before 1900
print("\nTitles and authors of all books where the author was born before 1900")
c.execute("""
        SELECT Books.Title, Authors.Name
        FROM Books
        INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID
        WHERE Authors.BirthDate < '1900-01-01'
          """)

for book, author in c.fetchall():
    print(f'{book} by {author}')

#  fetch the names of all authors and the genres of their books
print("\nNames of all authors and the genres of their books")
c.execute("""
        SELECT Authors.Name, Genres.Name
        FROM Authors
        INNER JOIN Books ON Authors.AuthorID = Books.AuthorID
        INNER JOIN Book_Genres ON Books.BookID = Book_Genres.BookID
        INNER JOIN Genres ON Book_Genres.GenreID = Genres.GenreID
          """)

for author, genre in c.fetchall():
    print(f'{author} has written books in the {genre} genre.')

# INSERT
# insert lord of the rings by J.R.R. Tolkien published in 1954
c.execute("INSERT INTO Authors (AuthorID, Name, BirthDate) VALUES (?, ?, ?)", (4, 'J.R.R. Tolkien', '1892-01-03'))
c.execute("INSERT INTO Books (Title, AuthorID, PublicationYear) VALUES (?, ?, ?)", ('The Lord of the Rings', 4, 1954))

# insert agartha christie in authors
c.execute("INSERT INTO Authors (AuthorID, Name, BirthDate) VALUES (?, ?, ?)", (5, 'Agatha Christie', '1890-09-15'))

# insert mystery genre in genres
c.execute("INSERT INTO Genres (GenreID, Name) VALUES (?, ?)", (4, 'Mystery'))

# insert a new book-genre relationship 6,3 
c.execute("INSERT INTO Book_Genres (BookID, GenreID) VALUES (?, ?)", (6, 3))

# insert a new borrower
c.execute("INSERT INTO Borrowers (BorrowerID, Name, Email) VALUES (?, ?, ?)", (4, 'Emily Johnson', 'emilyjohnson@example.com'))

conn.commit()

# DELETE
# delete a book and its book-genre relationship
c.execute("DELETE FROM Books WHERE BookID = 3")
c.execute("DELETE FROM Book_Genres WHERE BookID = 3")

# delete an author and their books
c.execute("DELETE FROM Authors WHERE AuthorID = 2")
c.execute("DELETE FROM Books WHERE AuthorID = 2")

# delete all books published before 1930
c.execute("DELETE FROM Book_Genres WHERE BookID IN (SELECT BookID FROM Books WHERE PublicationYear < 1930)")
c.execute("DELETE FROM Books WHERE PublicationYear < 1930")

# delete all genres and their book-genre relationships
c.execute("DELETE FROM Book_Genres")
c.execute("DELETE FROM Genres")

# not gonna commit these changes to keep the database intact for further queries


# INNER JOIN
# Books and authors
print("\nBooks and authors")
c.execute("""
        SELECT Books.Title, Authors.Name
        FROM Books
        INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID
          """)
for book, author in c.fetchall():
    print(f'{book} by {author}')
    
# Books, genre and authors
print("\nBooks, genre and authors")
c.execute("""
        SELECT Books.Title, Genres.Name, Authors.Name
        FROM Books
        INNER JOIN Book_Genres ON Books.BookID = Book_Genres.BookID
        INNER JOIN Genres ON Book_Genres.GenreID = Genres.GenreID
        INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID
          """)
for book, genre, author in c.fetchall():
    print(f'{book}, a {genre}, by {author}')


conn.close()