file_name = input("Enter a shopping list file: ")

items = []
with open(file_name, 'r') as f:
  file = f.readlines()
  for i in file:
    if i.strip() in items:
      continue
    else:
      items.append(i.strip())
items.sort()
print("Final list:")
for i in items:
  print(i.strip())
