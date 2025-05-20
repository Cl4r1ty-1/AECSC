def tax(subtotal):
    # add tax amount to subtotal
    TAX_PERCENTAGE = 0.1
    tax_amount = subtotal * TAX_PERCENTAGE
    total = subtotal + tax_amount
    return tax_amount, total

def discount(subtotal):
    # take discount from subtotal
    DISCOUNT = 0.1
    discount_subtotal = subtotal * DISCOUNT
    discount_total = subtotal - discount_subtotal
    return discount_total

def priority(quantity, subtotal):
    # add priority amount to subtotal
    PRIORITY = 2.0
    priority_subtotal = quantity * PRIORITY
    subtotal += priority_subtotal
    return subtotal

# define rides and prices in a list of dictionaries
rides = [
    {"name":"Ferris Wheel", "price":6.00, "count":0},
    {"name":"Roller Coaster", "price":8.50, "count":0},
    {"name":"Dodgem Cars", "price":5.50, "count":0}
    ]

# initialise variables
num_bookings = 0
total_made = 0.0

# welcome screen
print("======Welcome to Mindarie Carnival Rides!=======")
print("------Rides and ticket prices:------")
print("Ferris Wheel - $6.00 per ride")
print("Roller Coaster - $8.50 per ride")
print("Dodgem Cars - $5.50 per ride")
print()
print("------Extras and discounts------")
print("Priority Pass - $2.00 (per ride, per ticket")
print("10% discount when you buy 5 or more tickets!")
print()
print("All prices are not inclusive of GST")
print()

customers = "Y"
while customers == "Y":
    # combined_quantity = 0
    print()
    print("Options: ")
    print("1. Ferris Wheel")
    print("2. Roller Coaster")
    print("3. Dodgem Cars")
    
    ride = input("Enter the number of the ride you want to go on: ")
    while ride not in ["1", "2", "3"]:
        print("Invalid option!")
        ride = input("Enter the number of the ride you want to go on: ")
    quantity = int(input("How many tickets do you want for that ride? "))
    
    if ride == '1':
        subtotal = rides[0]["price"] * quantity # set subtotal to cost of tickets
        rides[0]["count"] += quantity # keep track of tickets sold for the ride
        ride_name = rides[0]["name"]
    elif ride == '2':
        subtotal = rides[1]["price"] * quantity
        rides[1]["count"] += quantity
        ride_name = rides[1]["name"]
    elif ride == '3':
        subtotal = rides[2]["price"] * quantity
        rides[2]["count"] += quantity
        ride_name = rides[2]["name"]
        
    # combined_quantity += quantity
    priority_quantity = int(input("How many priority passes do you want for these tickets? "))
    while priority_quantity > quantity: # don't allow user to have more priority passes than tickets
        print("You can't have more priority passes than tickets!")
        priority_quantity = int(input("How many priority passes do you want for these tickets? "))
    
    subtotal = priority(priority_quantity, subtotal) # add priority pass to subtotal
    
    if quantity >= 5:
        subtotal = discount(subtotal) # take discount from subtotal if buying 5 or more tickets
        
    tax_amount, total = tax(subtotal) # add tax amount
    total_made += total # keep track of amount made through the day
    
    print("======YOUR ORDER======")
    print(f"{quantity} tickets for the {ride_name}")
    print(f"{priority_quantity} priority passes for your tickets")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax: {tax_amount:.2f}")
    print(f"Total: {total:.2f}")
    
    num_bookings += 1 # keep track of bookings
    
    print()
    customers = input("Are there still customers? (Y or N) ").upper()
    while customers not in ["Y", "N"]:
        print("Type Y for yes, or N for no")
        customers = input("Are there still customers? (Y or N) ").upper()
print()
print(f"Number of bookings: {num_bookings}")
print(f"Ferris Wheel tickets sold: {rides[0]['count']}")
print(f"Roller Coaster tickets sold: {rides[1]['count']}")
print(f"Dodgem Cars tickets sold: {rides[2]['count']}")
print(f"Total money collected: {total_made:.2f}")
        