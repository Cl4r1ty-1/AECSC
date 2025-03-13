def filter_long_words(words):
    long_words = [word for word in words if len(word) > 5]
    return long_words

words = ["python", "programming", "challenge", "list", "comprehension"]
result = filter_long_words(words)
print(result)