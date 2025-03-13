def concatenate_strings(words):
    long_string = ", ".join([word for word in words])
    return long_string

words = ["apple", "banana", "orange", "kiwi"]
result = concatenate_strings(words)
print(result)