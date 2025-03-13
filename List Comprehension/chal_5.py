def concatenate_lists(list1, list2):
    new_list = list1 + list2
    long_string = ", ".join(word for word in new_list)
    return long_string

list1 = ["apple", "banana", "orange"]
list2 = ["kiwi", "pineapple", "mango"]
result = concatenate_lists(list1, list2)
print(result)