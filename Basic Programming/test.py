try:
    num = float(input("Enter a number: "))
    print(10/num)
except Exception as e:
    print(f"An error occurred: {e}")