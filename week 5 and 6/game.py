import random
while True:
    user_list =[]
    user_range = input("Level: ")
    if not user_range.isdigit():
        continue
    elif int(user_range) < 1:
        continue
    else:
        break

user_range = int(user_range)
user_list.extend(range(1,(user_range+1)))

target = random.choice(user_list)

while True:
    guess = input("Guess:")
    if not guess.isdigit():
        continue
    elif int(guess) <1:
        continue
    guess = int(guess)
    if guess == target:
        print("Just right!")
        exit()
    elif guess>target:
        print("Too large!")
    elif guess<target:
        print("Too small!")



