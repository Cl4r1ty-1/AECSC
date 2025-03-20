products = {
    "Apple":1.50,
    "Banana":0.80,
    "Milk":2.30,
    "Bread":3.00
}

cart = {}

print("Available Products:")
num = 1
for product, price in products.items():
    print(f"{num}. {product}: ${price:.2f}")
    num += 1

print()

product = input("Enter product name to add to cart (or 'done' to finish): ")
while product != "done":
    if product in products.keys():
        quantity = int(input("Enter quantity: "))
        if product in cart.keys():
            cart[product] = cart[product] + quantity
        else:
            cart[product] = quantity
    else:
        print("Enter a vaild product!")
    product = input("Enter product name to add to cart (or 'done' to finish): ")

total = 0
print()
print("Shopping Cart:")
for product, quantity in cart.items():
    print(f"{quantity} x {product} - ${(quantity*products[product]):.2f}")
    total += quantity*products[product]

print()
print(f"Total Cost: ${total:.2f}")