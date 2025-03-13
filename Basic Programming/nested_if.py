# Module to output whether user is an adult, teenager or child

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
elif age < 18 and age >= 13:
    print("You are a teenager")
elif age < 13 and age >= 0:
    print("You are a child")
else:
    print("Bro isn't born yet")