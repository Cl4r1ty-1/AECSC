from deck import deck
import random

class Player:
    def __init__(self, name: str, score: int, deck: list):
        self.name = name
        self.score = score
        self.deck = deck
    def __repr__(self):
        return self.name
    
class CPU(Player):
    pass

def get_player_deck() -> list:
    player_deck = [deck[-(i+1)] for i in range(7)]
    return player_deck

def get_players() -> list:
    player = input("Enter your player name: ")   
    cpus = int(input("Enter the number of computer generated players you would like to play against: "))
    players = [Player(player, 0, get_player_deck())] + [CPU(f'CPU{i+1}', 0, get_player_deck()) for i in range(cpus)]
    return players

def get_play_order() -> list:
    play_order = get_players()
    random.shuffle(play_order)
    return play_order
