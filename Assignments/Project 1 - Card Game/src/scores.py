import csv
import os

def save_to_file(winner, score, filename="leaderboard.csv"):
    entries = []
    # get current leaderboard
    try:
        with open(filename, 'r') as leaderboard_db:
            csv_reader = csv.reader(leaderboard_db)
            for row in csv_reader:
                entries.append((row[0], int(row[1])))
    except FileNotFoundError:
        # if leaderboard is not found, assume game has not been run before and create a leaderboard file
        print("No leaderboard file found. Writing to a new file!")

    # add new winner to the list of current winners as a tuple
    entries.append((winner, score))

    # sort the list based on the highest score (second element in the tuple) and get the top 5
    entries.sort(key=lambda x: x[1], reverse=True)
    top_5 = entries[:5]

    # open (or create) the leaderboard file to write to
    with open(filename, 'w+', newline='') as leaderboard_db:
        csv_write = csv.writer(leaderboard_db)
        for entry in top_5: # write the top 5 to the leaderboard
            csv_write.writerow(entry)

def get_scores(filename="leaderboard.csv"):
    print("Top 5 players:")
    try:
        # display leaderboard
        with open(filename, 'r') as leaderboard_db:
            csv_reader = csv.reader(leaderboard_db)
            no = 1
            for row in csv_reader:
                print(f"{no}. {row[0]} scored {row[1]} cards!")
                no += 1
    except FileNotFoundError:
        print("No leaderboard file found!")
        print("Ensure you are in the project directory and have played at least once.")
