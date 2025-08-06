from random import randint


def main():
    level = get_level()
    correct = 0
    for _ in range(10):
        a, b = generate_integer(level)
        counter =0
        while counter<3:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer ==(a+b):
                    correct +=1
                    break
                else:
                    print("EEE")
                    counter+=1
            except ValueError:
                print("EEE")
                counter+=1
        if counter==3:
            print(f"{a}+{b}={a+b}")
    print(f"Score: {correct}")


def get_level():
    levels = [1, 2, 3]
    while True:
        level = input("Level: ")
        if not level.isdigit() or (int(level) not in levels):
            continue
        else:
            break
    level = int(level)
    return level

def generate_integer(level):
    if level == 1:
        a = randint(0, 9)
        b = randint(0, 9)
    elif level == 2:
        a = randint(10, 99)
        b = randint(10, 99)
    elif level == 3:
        a = randint(100, 999)
        b = randint(100, 999)
    return a,b

if __name__ == "__main__":
    main()