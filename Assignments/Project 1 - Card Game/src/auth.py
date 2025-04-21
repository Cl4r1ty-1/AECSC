def authenticate(filename="users.txt"):
    # Get authorized users from file
    users = []
    with open(filename, 'r') as user_db:
        user_record = user_db.readlines()
        for user in user_record:
            users.append(user.strip())

    # Get user's names
    player1 = input("Enter player 1's name: ").title()
    player2 = input("Enter player 2's name: ").title()

    auth = False
    while not auth:
    # Check if users are authorized
        if player1 in users:
            if player2 in users:
                auth = True
            else:
                print("Player 2 is not authorized! Try again!")
                player2 = input("Enter player 2's name: ").title()
        else:
            print("Player 1 is not authorized! Try again!")
            player1 = input("Enter player 1's name: ").title()
    print()
    return auth, player1, player2

if __name__ == "__main__":
    authenticate()
