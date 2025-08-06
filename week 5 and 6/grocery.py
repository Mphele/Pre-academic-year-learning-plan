user_list =[]
singles =[]

while True:
    try:
        user = input("")
        user_list.append(user)
    except EOFError:
        break

for item in user_list:
    if item not in singles:
        singles.append(item)

for fruit in sorted(singles):
    print(f"{user_list.count(fruit)} {fruit.upper()}")