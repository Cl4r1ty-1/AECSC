# This module asks the user 10 math questions and times their completion

import random
import time

operators = ["+", "-", "*"]

st = time.time() # start timing the user

for i in range(1, 11): # gives the user 10 questions
    # Get random integers for the question
    num1 = random.randint(3, 12)
    num2 = random.randint(3, 12)

    # Get random operation for the question
    operator = random.choice(operators)

    print(f"Question {i}: {num1} {operator} {num2}")

    try:
        answer = int(input("Enter your answer: "))
    except ValueError:
        print("Invalid answer!")
        answer = int(input("Enter your answer: "))

        # Check if the answer is correct, if not continue asking
    while answer != eval(f"{num1} {operator} {num2}"):
        try:
            print("Incorrect")
            answer = int(input("Enter your answer: "))
        except ValueError:
            print("Invalid answer!")
            continue
    
    print("Correct")

et = time.time() # finish timing the user

elapsed_time = round(et - st,2) # calculate user's time to 2 decimal places
print(f"You completed the challenge in: {elapsed_time} seconds!")