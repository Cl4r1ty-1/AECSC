from deck import deck, colours
from players import get_play_order
import random
import sys

def main_menu() -> None:
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

def authenticate(filename) -> None:
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

def play_game():
    global PLAY_ORDER
    global turn_order
    global play_colour
    PLAY_ORDER = get_play_order()
    turn_order = PLAY_ORDER
    played_card = deck[0]
    deck.pop(0)
    print(f'A {played_card} card was played')
    while played_card.type == "Wild":
        print("Can't start on a wild card!")
        deck.append(played_card)
        played_card = deck[0]
        deck.pop(0)
    play_colour = played_card.colour
    check_card(played_card)

def init_turn(played_card):
    global turn_order
    global play_colour
    if len(turn_order) == 0:
        print("Game Over!")
        end_game()
        return
    current_player = turn_order[0]
    print(f"It's {current_player.name}'s turn!")
    print(f"Current colour: {play_colour}")
    print(f"Current card: {played_card}")
    if current_player.is_cpu:
        chosen_card = random.choice(current_player.deck)
        print(f"{current_player.name} played {chosen_card}")
        current_player.deck.remove(chosen_card)
    else:
        chosen_card = input("Enter the card you want to play (or 'Draw' a card): ").title()
        while chosen_card not in current_player.deck:
            print("Invalid card! Try again.")
            played_card = input("Enter the card you want to play: ")
        while chosen_card not (played_card.type in chosen_card or played_card.colour in chosen_card): # fix this
            print("Invalid card! Try again.")
            chosen_card = input("Enter the card you want to play: ").title()
        current_player.deck.remove(played_card)
    
    check_card(played_card)


def check_card(played_card):
    global play_colour
    global turn_order
    if played_card.colour == "Wild":
        if turn_order[0].is_cpu:
            play_colour = random.choice(colours)
        else:
            colour_choice = input("Choose colour (Blue, Green, Yellow or Red): ").title()
            while colour_choice not in colours:
                print("Invalid Colour!")
                colour_choice = input("Choose colour (Blue, Green, Yellow or Red): ").title()
            play_colour = colour_choice

        if played_card.type == "Draw Four":
            for _ in range(4):
                turn_order[1].deck.append(deck[0])
                deck.pop(0)
            turn_order.pop(1)
    if played_card.type == "Draw Two":
        for _ in range(2):
            turn_order[1].deck.append(deck[0])
            deck.pop(0)
        turn_order.pop(1)
    if played_card.type == "Skip":
        turn_order.pop(1)
    if played_card.type == "Reverse":
        turn_order.reverse()

def end_game():
    pass

def get_scores():
    pass

if __name__ == '__main__':
    main_menu()
