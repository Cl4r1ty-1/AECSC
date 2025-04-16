from deck import deck, UnoCard
import random
import sys

def main_menu():
    # Print menu screen
    print("Welcome to UNO!")
    print()
    print("Please select an option")
    print("1. Play game")
    print("2. Display Scores")
    print("3. Exit")

    # Get user option
    option = input("> ")
    while True:
        if option == '1':
            authenticate('users.txt')
            break
        elif option == '2':
            get_scores()
            break
        elif option == '3':
            print("Thanks for playing!")
            sys.exit() # exit program
        else:
            print("Invalid Option!")
            option = input("> ")

def get_play_order():
    players = []
    player = input("Enter a player name: ")
    bots = int(input("Enter the number of computer opponents to play against: "))
    return players

def play_game():
    play_order = get_play_order()
    

def get_scores():
    pass

def authenticate(filename):
    while True:
        try:
            with open(filename, 'r') as f:
                users = f.readlines()
                user_db = [user.strip() for user in users]
                break
        except FileNotFoundError:
            print("users.txt not found! Enter the full path of the file and/or press enter to try again.")
            filename = input("> ")
            if filename == '':
                filename = 'users.txt'


    username = input("Enter your name to login: ")
    while username not in user_db:
        print("You are not authorized to play this game. Try again.")
        username = input("Enter your name to login: ")
    print("Authenticated!")
    print()
    play_game()

if __name__ == '__main__':
    main_menu()
