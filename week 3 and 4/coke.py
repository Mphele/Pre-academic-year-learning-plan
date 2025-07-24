#while loop that breaks when amount due reaches 0
#after that print change i change is bigger than 0
due = 50
while True:
    print(f"Amount due: {due}")
    user_insert = int(input("Insert Coin: "))
    if user_insert == 10 or  user_insert == 5  or user_insert == 25:
        due -= user_insert
    if due <= 0:
        change = due * -1
        break

print(f"Change Owed: {change}")