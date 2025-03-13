# This module takes 2 random float numbers, asks the user what operation to apply to them and outputs the answer
import random

# Get 2 random float values
num1 = round(random.uniform(1.0,10.0), 2)
num2 = round(random.uniform(1.0,10.0), 2)

# Shows the values to the user
print(f"Random float values: {num1}, {num2}")

operation = input("Enter an arithmatic operation (+,-,*,/,MOD): ").upper().strip()

# Perform the operation
try:
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "/":
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    elif operation == "MOD" or operation == "%":
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
    else:
        print("Invalid Operation")
except ZeroDivisionError:
    print("Division by zero is not allowed")