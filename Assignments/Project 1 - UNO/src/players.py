from deck import deck
import random

class Player:
    def __init__(self, name: str, is_cpu: bool, score: int, games_won: int, deck: list):
        self.name = name
        self.is_cpu = is_cpu
        self.score = score
        self.games_won = games_won
        self.deck = deck
    def __repr__(self):
        return self.name
    
def get_player_deck() -> list:
    player_deck = []
    for _ in range(7):
        player_deck.append(deck[0])
        deck.pop(0)
    return player_deck

def get_players() -> list:
    player = input("Enter your player name: ")   
    cpus = int(input("Enter the number of computer generated players you would like to play against: "))
    players = [Player(player, False, 0, 0, get_player_deck())] + [Player(f'CPU{i+1}', True, 0, 0, get_player_deck()) for i in range(cpus)]
    return players

def get_play_order() -> list:
    play_order = get_players()
    random.shuffle(play_order)
    return play_order
