import csv
import sqlite3

conn = sqlite3.connect('elden_ring.py')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Enemies")
c.execute("DROP TABLE IF EXISTS Weapons")
c.execute("DROP TABLE IF EXISTS Battles")

c.execute("""
          CREATE TABLE Enemies (
            EnemyID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Type TEXT,
            HP INTEGER
          )
          """)

c.execute("""
          CREATE TABLE Weapons (
            WeaponID INTEGER PRIMARY KEY,
            WeaponName TEXT NOT NULL,
            Damage INTEGER
          )
          """)

c.execute("""
          CREATE TABLE Battles (
            BattleID INTEGER PRIMARY KEY,
            EnemyID INTEGER,
            WeaponID INTEGER,
            Result TEXT,
            FOREIGN KEY (EnemyID) REFERENCES Enemies (EnemyID),
            FOREIGN KEY (WeaponID) REFERENCES Weapons (WeaponID)
          )
          """)

with open('enemies.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Enemies (EnemyID, ")
