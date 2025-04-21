import random

def get_deck():
    # init constants for colours and numbers
    COLOURS = ["Red", "Black", "Yellow"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    deck = [] # init list for deck
    for colour in COLOURS:
        for number in NUMBERS:
            card = {"colour":colour, "number":number} # cards are a dictionary
            deck.append(card) # the deck is a list of dictionaries
    
    random.shuffle(deck) # shuffle the deck
    return deck

# debugging stuff
if __name__ == "__main__":
    print(get_deck())
