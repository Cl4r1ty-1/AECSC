def get_string_lengths(strings):
    lengths = [len(s) for s in strings]
    return lengths

strings = ["apple", "banana", "orange", "kiwi"]
result = get_string_lengths(strings)
print(result)