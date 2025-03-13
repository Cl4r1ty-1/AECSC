def camel_case_to_sentence(input_string):
    words = [" " + char.lower() if char.isupper() else char for char in input_string]
    return ''.join(words)

input_string = "camelCaseWordsAreFun"
result = camel_case_to_sentence(input_string)
print(result)