from players import Player
import csv

def get_player_db() -> list:
    player_db = []
    with open("players.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            player_db.append(Player(row[0], row[1], []))
    return player_db
