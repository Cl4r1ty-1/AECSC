from auth import authenticate
from deck import get_deck
from winner import get_winner, get_overall_winner
from scores import get_scores, save_to_file
import sys

def main_menu():
    # init global vars
    global player1
    global player2

    print("Welcome to the card game!")
    # main menu loop
    while True:
        print()
        print("Please select an option")
        print("1. Play game")
        print("2. Display scores")
        print("3. Exit")
        option = input("> ")
        if option == '1':
            auth, player1, player2 = authenticate() # get player names from auth module
            # If users are authorized then play the game
            if auth:
                deck = get_deck()
                player1_deck, player2_deck = play_game(deck) # the main game function returns the player's decks for processing in the winner function
                winner, score = get_overall_winner(player1, player2, player1_deck, player2_deck)
                print()
                print("Saving winner to leaderboard file!")
                print()
                save_to_file(winner, score)
                print("Done!")
        elif option == '2':
            # print top 5 leaderboard
            print()
            get_scores()
        elif option == '3':
            print("Thanks for playing!")
            sys.exit() # exit program
        else:
            # if input invalid then keep asking for a valid option
            print("Invalid Option!")

def play_game(deck):
    # init player decks
    player1_deck = []
    player2_deck = []

    print("Game is starting!")
    round_number = 0
    while deck: # continue until deck is empty
        round_number += 1
        print(f"Round number {round_number}")
        print()
        print(f"It is {player1}'s turn!")
        print("Press enter to draw a card!")
        input("> ")

        card1 = deck.pop(0) # take a card from the top of the deck, this also removes it from the deck
        print(f"{player1} drew a {card1['colour']} {card1['number']}")
        print()

        print(f"It is {player2}'s turn!")
        print("Press enter to draw a card!")
        input("> ")

        card2 = deck.pop(0)
        print(f"{player2} drew a {card2['colour']} {card2['number']}")
        print()

        winner = get_winner(card1, card2)
        # process result of winner function
        if winner == 1:
            # add both cards to the winning player's deck
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
    # return player's decks for processing
    return player1_deck, player2_deck


if __name__ == "__main__":
    main_menu()
