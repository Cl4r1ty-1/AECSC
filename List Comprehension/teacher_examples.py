squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

squares = [i ** 2 for i in range(1, 6)]
print(squares)

evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
print(evens)

evens = [i for i in range(10) if i % 2 == 0]
print(evens)