from auth import authenticate
from deck import get_deck
from winner import get_winner, get_overall_winner
from scores import get_scores, save_to_file
import sys

def main_menu():
    global player1
    global player2

    print("Welcome to the card game!")
    print()
    print("Please select an option")
    print("1. Play game")
    print("2. Display scores")
    print("3. Exit")
    
    option = input("> ")
    while True:
        if option == '1':
            auth, player1, player2 = authenticate()
            # If users are authorized then play the game
            if auth:
                deck = get_deck()
                player1_deck, player2_deck = play_game(deck)
                winner, score = get_overall_winner(player1, player2, player1_deck, player2_deck)
                print()
                print("Saving winner to leaderboard file!")
                print()
                save_to_file(winner, score)
                print("Done!")
            break
        elif option == '2':
            print()
            get_scores()
            break
        elif option == '3':
            print("Thanks for playing!")
            sys.exit() # exit program
        else:
            # if input invalid then keep asking for a valid option
            print("Invalid Option!")
            option = input("> ")

def play_game(deck):
    player1_deck = []
    player2_deck = []

    print("Game is starting!")
    round_number = 0
    while deck:
        round_number += 1
        print(f"Round number {round_number}")
        print()
        print(f"It is {player1}'s turn!")
        print("Press enter to draw a card!")
        input("> ")

        card1 = deck.pop(0)
        print(f"{player1} drew a {card1['colour']} {card1['number']}")
        print()

        print(f"It is {player2}'s turn!")
        print("Press enter to draw a card!")
        input("> ")

        card2 = deck.pop(0)
        print(f"{player2} drew a {card2['colour']} {card2['number']}")
        print()

        winner = get_winner(card1, card2)
        if winner == 1:
            player1_deck.append(card1)
            player1_deck.append(card2)
            print(f"{player1} won this round!")
        else:
            player2_deck.append(card1)
            player2_deck.append(card2)
            print(f"{player2} won this round!")
        print()

        print("Press enter to continue")
        input("> ")
    print("No more cards. Game over!")
    print()
    return player1_deck, player2_deck


if __name__ == "__main__":
    main_menu()
