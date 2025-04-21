import random

def get_deck():
    COLOURS = ["Red", "Black", "Yellow"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    deck = []
    for colour in COLOURS:
        for number in NUMBERS:
            card = {"colour":colour, "number":number}
            deck.append(card)
    
    random.shuffle(deck)
    return deck

if __name__ == "__main__":
    print(get_deck())
