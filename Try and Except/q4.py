try:
    file_input = input("Enter a filename: ").strip()
    with open(file_input, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file doesn't exist!")
except IOError:
    print("Try a different file!")