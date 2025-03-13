print("This program will divide 2 the first number by the second number")

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1/num2
except ZeroDivisionError:
    print("You can't divide by Zero!")
except ValueError:
    print("Invalid input!")
else:
    print(f"Result: {num1}/{num2} is {result}")