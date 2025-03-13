# This module lets the user play a simple rock paper scissors game against the computer

import random

options = ['rock', 'paper', 'scissors']
win = 0
loss = 0
tie = 0

winning_moves = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

player_choice = input("Rock, Paper, Scissors (Enter 'q' to quit): ").lower().strip()

while player_choice != 'q':
    computer_choice = random.choice(options)
    if player_choice not in options:
        print("Invalid Input!")
    else:
        if player_choice == computer_choice:
            print(f"Computer chose {computer_choice}")
            print("It's a tie!")
            tie += 1
        elif winning_moves[player_choice] == computer_choice:
            print(f"Computer chose {computer_choice}")
            print("You win!")
            win += 1
        else:
            print(f"Computer chose {computer_choice}")
            print("You lose!")
            loss += 1
    player_choice = input("Rock, Paper, Scissors (Enter 'q' to quit): ")

print(f"Player won {win} times!")
print(f"Computer won {loss} times!")
print(f"You tied {tie} times!")