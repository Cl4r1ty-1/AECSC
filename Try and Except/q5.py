try:
    numbers = input("Enter a list of number separated by spaces: ")

    num_list = numbers.split(' ')
    num_list = [float(i) for i in num_list]

    average = sum(num_list)/len(num_list)

    print(f"Average: {average}")
except ZeroDivisionError:
    print("You can divide by Zero!")
except ValueError:
    print("Please on;y enter number values")
except:
    print("Something went wrong")
    