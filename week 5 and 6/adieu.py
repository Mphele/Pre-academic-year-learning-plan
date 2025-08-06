user_list = []

while True:
    try:
        user = input(": ").title()
        user_list.append(user)
    except EOFError:
        break

if len(user_list) == 1:
    print(f"Adieu, adieu, to {user_list[0]}")
elif len(user_list)==2:
    print(f"Adieu, adieu, to {user_list[0]} and {user_list[1]}" )
elif len(user_list) > 2:
    print("Adieu, adieu, to ", end="")
    for name in range(len(user_list) - 1):
        print(f"{user_list[name]}, ", end="")
    print(f"and {user_list[-1]}")
