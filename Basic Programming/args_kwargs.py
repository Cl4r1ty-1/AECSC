def add(a, b):
    return a + b

print(add(4,3))

def add2(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add2(1, 4, 6, 10, 15, 15))

def add2(*args):
    return sum([arg for arg in args])


def print_address(**kwargs):
    for key in kwargs.keys():
        print(key)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(place = "Mindarie Senior College",
              address = "14 Elliston Parade",
              )


def teaching_staff(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    for value in kwargs.values():
        print(value, end=' ')