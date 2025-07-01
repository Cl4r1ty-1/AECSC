import csv
import sqlite3

conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Pokemon')
c.execute('DROP TABLE IF EXISTS Battles')

c.execute("""
          CREATE TABLE Pokemon (
              PokemonID INTEGER PRIMARY KEY,
              Name TEXT,
              Type TEXT,
              BaseAttack INTEGER
          )
          """
          )


c.execute("""
          CREATE TABLE Battles (
              BattleID INTEGER PRIMARY KEY,
              PokemonID INTEGER,
              OpponentID INTEGER,
              Result TEXT,
              FOREIGN KEY (PokemonID) REFERENCES Pokemon (PokemonID),
              FOREIGN KEY (OpponentID) REFERENCES Pokemon (PokemonID)
          )
          """
          )

with open('pokemons.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Pokemon (PokemonID, Name, Type, BaseAttack) VALUES (?, ?, ?, ?)", row)
        
with open('battles.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        c.execute("INSERT INTO Battles (BattleID, OpponentID, PokemonID, Result) VALUES (?, ?, ?, ?)", row)

conn.commit()
print("Successfully created database and inserted csv data")

print("1. SELECT all pokemon")
c.execute("SELECT * FROM Pokemon")
for row in c.fetchall():
    print(row)

print("\n2. INSERT snorlax")
new_pokemon_data = ("Snorlax", "Normal", 110)
c.execute("INSERT INTO Pokemon (Name, Type, BaseAttack) VALUES (?, ?, ?)", new_pokemon_data)
conn.commit()
print(f"Successfully added '{new_pokemon_data[0]}' to Pokemon table")

print("3. DELETE Gengar battle records")
pokemon_to_delete = 5
c.execute(f"DELETE FROM Battles WHERE PokemonID = {pokemon_to_delete}")
conn.commit()
print("Deleted Gengar battle records")

print("4. Update Pikachu's Base Attack")
new_base_attack = 60
c.execute(f"UPDATE Pokemon SET BaseAttack = {new_base_attack} WHERE Name = 'Pikachu'")
conn.commit()
print(f"Updated Pikachu's base attack to {new_base_attack}")

print("\n5. Order by Base Attack descending")
c.execute("SELECT * FROM Pokemon ORDER BY BaseAttack DESC")
for row in c.fetchall():
    print(row)

print("\n6. INNER JOIN Pokemon Battles") # ask about opponent name
c.execute("""
        SELECT Pokemon.Name, Pokemon.Type, Battles.OpponentID, Battles.Result
        FROM Battles
        INNER JOIN Pokemon ON Battles.PokemonID = Pokemon.PokemonID
          """)
for row in c.fetchall():
    print(row)

print("\n7. COUNT total battles")
c.execute("SELECT COUNT(*) FROM Battles")
print(c.fetchone()[0])

print("\n8. SUM of all Base Attacks")
c.execute("SELECT SUM(BaseAttack) FROM Pokemon")
print(c.fetchone()[0])

print("\n9. AVERAGE Base Attack")
c.execute("SELECT AVG(BaseAttack) FROM Pokemon")
print(int(c.fetchone()[0]))

print("\n10. MIN and MAX Base Attacks")
c.execute("SELECT MIN(BaseAttack) FROM Pokemon")
print(f"Min: {c.fetchone()[0]}")
c.execute("SELECT MAX(BaseAttack) FROM Pokemon")
print(f"Max: {c.fetchone()[0]}")