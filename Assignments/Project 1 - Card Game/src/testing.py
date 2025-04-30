from winner import get_winner, get_overall_winner
import unittest

import sys

# modified auth to take users as paramaters
def authenticate(player1, player2, filename="users.txt"):
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

    # Check if users are authorized, if not specify which one and let user try again
    if player1 in users:
        if player2 in users:
            auth = True
        else:
            auth = False
    else:
        auth = False
    print()
    return auth

class TestModules(unittest.TestCase):
    def test_auth(self):
        auth = authenticate("Ben Thomas", "Oliver Sykes")
        self.assertEqual(auth, True, "Fail")
        auth = authenticate("John Doe", "Ben Thomas")
        self.assertEqual(auth, False, "Fail")
        auth = authenticate("John Doe", "Jane Doe")
        self.assertEqual(auth, False, "Fail")
        auth = authenticate("Ben Thomas", "John Doe")
    
    def test_winner(self):
        test1 = get_winner({"colour":"Red","number":9}, {"colour":"Yellow","number":5})
        test2 = get_winner({"colour":"Black","number":3}, {"colour":"Yellow","number":8})
        test3 = get_winner({"colour":"Red","number":9}, {"colour":"Red","number":5})
        self.assertEqual(test1, 2, "Fail")
        self.assertEqual(test2, 1, "Fail")
        self.assertEqual(test3, 1, "Fail")

    def test_overall_winner(self):
        test1, score1 = get_overall_winner("1", "2", range(14), range(16))
        test2, score2 = get_overall_winner("1", "2", range(16), range(14))
        test3, score3 = get_overall_winner("1", "2", range(15), range(15))
        self.assertEqual(test1, '2', "Fail")
        self.assertEqual(test2, '1', "Fail")
        self.assertEqual(test3, None, "Fail")
        self.assertEqual(score1, 16, "Fail")
        self.assertEqual(score2, 16, "Fail")
        self.assertEqual(score3, None, "Fail")

if __name__ == '__main___':
    unittest.main()