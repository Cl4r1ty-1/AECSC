import random

class UnoCard:
    def __init__(self, colour: str, type: str):
        self.colour = colour
        self.type = type
    def __repr__(self):
        return f'{self.colour} {self.type}'
    
    def __eq__(self, other):
        if isinstance(other, UnoCard):
            return self.colour == other.colour and self.type == other.type
        return False

    def __hash__(self):
        return hash((self.colour, self.type))
 
COLOURS = ['Blue', 'Green', 'Red', 'Yellow']
types = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Draw Two', 'Reverse']
types = sorted(types + types)[1:]

deck = [UnoCard(c, t) for c in COLOURS for t in types] + \
    [UnoCard('Wild', 'Wild') for _ in range (4)] + \
    [UnoCard('Wild', 'Draw Four') for _ in range(4)]

random.shuffle(deck)

