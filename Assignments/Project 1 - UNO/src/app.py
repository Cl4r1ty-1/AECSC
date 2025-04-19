from deck import deck, COLOURS, UnoCard
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


    username = input("Enter your name to login: ").title()
    while username not in user_db:
        print("You are not authorized to play this game. Try again.")
        username = input("Enter your name to login: ").title()
    print("Authenticated!")
    print()
    play_game()

def play_game():
    global play_order
    global turn_order
    global play_colour
    global played_card
    play_order = get_play_order()
    turn_order = play_order[:]
    print("\nGame is starting!\n")

    played_card = deck[0]
    deck.pop(0)
    print(f'A {played_card} was played to start')
    while played_card.type == "Wild":
        print("Can't start on a wild card!")
        deck.append(played_card)
        played_card = deck[0]
        deck.pop(0)
        print(f'A {played_card} was played to start')
    play_colour = played_card.colour
    check_card(played_card, is_start=True)
    print()
    
    while True:
        for current_player in turn_order[:]:
            init_turn(current_player)

            if not current_player.deck:
                end_game()

            if turn_order != play_order:
                break

        turn_order = play_order[:]

def init_turn(current_player):
    global played_card
    global play_colour
    print(f"\nIt is {current_player.name}'s turn!\n")
    
    # CPU turn logic
    if current_player.is_cpu:
        # Check if the CPU has a playable card
        playable_cards = [
            card for card in current_player.deck
            if card.colour == play_colour or card.type == played_card.type or card.colour == "Wild"
        ]

        if playable_cards:
            chosen_card = random.choice(current_player.deck)
            print(f"{current_player.name} played a {chosen_card}!")
            current_player.deck.remove(chosen_card)
            check_card(chosen_card)
            played_card = chosen_card
            play_colour = played_card.colour
        else:
            # Draw a card from the deck
            print(f"{current_player.name} has no playable cards and draws a card.")
            drawn_card = deck[0]
            deck.pop(0)
            current_player.deck.append(drawn_card)
            print(f"{current_player.name} drew a {drawn_card}.")

            # Check if the drawn card is playable
            if drawn_card.colour == play_colour or drawn_card.type == played_card.type or drawn_card.colour == "Wild":
                print(f"{current_player.name} played the drawn card: {drawn_card}!")
                current_player.deck.remove(drawn_card)
                check_card(drawn_card)
                played_card = drawn_card
                play_colour = played_card.colour
            else:
                print(f"{current_player.name} cannot play the drawn card.")
    
    # Player turn logic
    else:
        str_deck = [str(i) for i in current_player.deck]
        print(f'Your deck: {str_deck}')
        print(f'Played card: {played_card}')
        
        while True:
            print("What would you like to do?")
            print("1. Play a card")
            print("2. Draw a card from the deck")
            option = input("> ")

            if option == "1":
                print("Select the card you would like to play. (Type card name as shown in deck)")
                chosen_card_str = input("> ")
                if chosen_card_str in str_deck:

                    chosen_card = next(card for card in current_player.deck if str(card) == chosen_card_str)

                    if chosen_card.colour == play_colour or chosen_card.type == played_card.type:
                        print(f"You played a {chosen_card}!")
                        current_player.deck.remove(chosen_card)
                        check_card(chosen_card)
                        played_card = chosen_card
                        play_colour = played_card.colour
                        break
                    else:
                        print("Can't play that card!") 
                else:
                    print("You don't have that card!")
            elif option == "2":
                # Draw a card from the deck
                print("You draw a card.")
                drawn_card = deck[0]
                deck.pop(0)
                current_player.deck.append(drawn_card)
                print(f"{current_player.name} drew a {drawn_card}.")

                # Check if the drawn card is playable
                if drawn_card.colour == play_colour or drawn_card.type == played_card.type or drawn_card.colour == "Wild":
                    print(f"{current_player.name} played the drawn card: {drawn_card}!")
                    current_player.deck.remove(drawn_card)
                    check_card(drawn_card)
                    played_card = drawn_card
                    play_colour = played_card.colour
                break
            else:
                print("Invalid option!")

def check_card(played_card, is_start=False):
    global play_colour
    global turn_order
    global play_order
    if played_card.colour == "Wild":
        if turn_order[0].is_cpu:
            play_colour = random.choice(COLOURS)
        else:
            colour_choice = input("Choose colour (Blue, Green, Yellow or Red): ").title()
            while colour_choice not in COLOURS:
                print("Invalid Colour!")
                colour_choice = input("Choose colour (Blue, Green, Yellow or Red): ").title()
            play_colour = colour_choice
            print(f"Play colour is now {play_colour}!")

        if played_card.type == "Draw Four":
            for _ in range(4):
                turn_order[1].deck.append(deck[0])
                deck.pop(0)
            turn_order.pop(1)
    elif played_card.type == "Draw Two":
        if not is_start:
            for _ in range(2):
                turn_order[1].deck.append(deck[0])
                deck.pop(0)
            turn_order.pop(1)
            print(f"{turn_order[1].name} drew 2 cards and is skipped!")
        else:
            for _ in range(2):
                turn_order[0].deck.append(deck[0])
                deck.pop(0)
            turn_order.pop(0)
            print(f"{turn_order[0].name} drew 2 cards and is skipped!")
    elif played_card.type == "Skip":
        if not is_start:
            turn_order.pop(1)
        else:
            turn_order.pop(0)
    elif played_card.type == "Reverse":
        turn_order.reverse()
        play_order.reverse()

def end_game():
    pass

def get_scores():
    pass

if __name__ == '__main__':
    main_menu()
