def get_even_numbers(numbers):
    even_numbers = [i for i in numbers if i % 2 == 0]
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_even_numbers(numbers)
print(result)