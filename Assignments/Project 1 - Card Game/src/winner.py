def get_winner(card1, card2):
    # If cards are same colour then the higher number wins
    if card1["colour"] == card2["colour"]:
        if card1["number"] > card2["number"]:
            return 1
        else:
            return 2
    
    # Colour rules
    colour_win = {
        "Red": "Black",
        "Yellow": "Red",
        "Black": "Yellow"
    }

    # if the cards are different colours, compare them by colour
    if colour_win[card1["colour"]] == card2["colour"]:
        return 1
    else:
        return 2

def get_overall_winner(player1, player2, player1_deck, player2_deck):
    # get player's score based on how many cards they won
    player1_score = len(player1_deck)
    player2_score = len(player2_deck)
    
    print(f"{player1} won {player1_score} cards.")
    print(f"{player2} won {player2_score} cards.")

    if player1_score > player2_score:
        winner = player1
        score = player1_score
        print(player1 + " wins!")
        return winner, score
    elif player1_score < player2_score:
        winner = player2
        score = player2_score
        print(player2 + " wins!")
        return winner, score
    else:
        print("Its a tie!")
        return None, None
    
if __name__ == "__main__":
    print(get_overall_winner("1", "2", range(16), range(14)))