import csv
import os

def save_to_file(winner, score, filename="leaderboard.csv"):
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as leaderboard_db:
            csv_reader = csv.reader(leaderboard_db)
            for row in csv_reader:
                entries.append((row[0], int(row[1])))
    else:
        print("No leaderboard file found! Writing to new file!")

    entries.append((winner, score))

    entries.sort(key=lambda x: x[1], reverse=True)
    top_5 = entries[:5]

    with open(filename, 'w+', newline='') as leaderboard_db:
        csv_write = csv.writer(leaderboard_db)
        for entry in top_5:
            csv_write.writerow(entry)

def get_scores(filename="leaderboard.csv"):
    print("Top 5 players:")
    try:
        with open(filename, 'r') as leaderboard_db:
            csv_reader = csv.reader(leaderboard_db)
            no = 1
            for row in csv_reader:
                print(f"{no}. {row[0]} scored {row[1]} cards!")
                no += 1
    except FileNotFoundError:
        print("No leaderboard file found!")
