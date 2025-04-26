import sys

def authenticate(filename="users.txt"):
    # Get authorized users from file
    while True:
        try:
            with open(filename, 'r') as user_db:
                user_record = user_db.readlines()
                users = [user.strip() for user in user_record]
                break
        except FileNotFoundError:
            print("No users file found!")
            print("Ensure you are in the project directory.")
            print("Press enter to try again or type exit and press enter to exit.")
            option = input("> ").lower()
            if option == "exit":
                sys.exit()

    # Get user's names
    player1 = input("Enter player 1's name: ").title()
    player2 = input("Enter player 2's name: ").title()

    while player1 == player2:
        print("Both players cannot have the same name!")
        player1 = input("Enter player 1's name: ").title()
        player2 = input("Enter player 2's name: ").title()

    auth = False
    while not auth:
    # Check if users are authorized, if not specify which one and let user try again
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

# debugging stuff
if __name__ == "__main__":
    authenticate()
