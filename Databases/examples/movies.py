import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

#drop tables if the already exist
cursor.execute("DROP TABLE IF EXISTS Castings")
cursor.execute("DROP TABLE IF EXISTS Actors")
cursor.execute("DROP TABLE IF EXISTS Movies")

#create movies table
cursor.execute("""
            CREATE TABLE Movies (
               MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
               Title TEXT NOT NULL,
               Genre TEXT,
               ReleaseYear INTEGER,
               BoxOffice REAL,
               IsSequel BOOLEAN
               )
               """)

#create an actors table
cursor.execute("""
            CREATE TABLE Actors (
               ActorID INTEGER PRIMARY KEY AUTOINCREMENT,
               FirstName TEXT NOT NULL,
               LastName TEXT NOT NULL,
               BirthDate DATE,
               Nationality TEXT
               )
               """)

#create a casting table
cursor.execute("""
            CREATE TABLE Castings (
               CastingID INTEGER PRIMARY KEY AUTOINCREMENT,
               ActorID INTEGER,
               MovieID INTEGER,
               RoleName TEXT,
               Pay REAL (10, 2),
               FOREIGN KEY (MovieID) REFERENCES Movies (MovieID),
               FOREIGN KEY (ActorID) REFERENCES Actors (ActorID)
               )
               """)

#insert data into movies table
cursor.executemany("""
            INSERT INTO Movies(Title, Genre, ReleaseYear, BoxOffice, IsSequel)
            VALUES
            ('The Matrix', 'SciFi', 1999, 46351783.00, 0),
            ('The Matrix: Reloaded', 'SciFi', 2003, 738576920.00, 1)
               """)

#insert data into actors table
cursor.execute("""
            INSERT INTO Actors(FirstName, LastName, BirthDate, Nationality)
            VALUES
            ('Keanu', 'Reeves', '02-09-1964', 'Canadian'),
            ('Carrie-Anne', 'Moss', '21-08-1967', 'Canadian')
               """)

#insert data into casting table
cursor.execute("""
            INSERT INTO Castings(ActorID, MovieID, RoleName, Pay)
            VALUES
            (1, 1, 'Neo', 30000000.00),
            (2, 1, 'Trinity', 10000000.00),
            (1, 2, 'Neo', 30000000.00)
               """)

#commit and close
conn.commit()
conn.close()

print("Database created and populated successfully")