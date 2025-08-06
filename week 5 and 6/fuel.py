import math
while True:
    try:
        usr = input("Fraction: ").strip()
        x, y = usr.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            continue

        if x > y:
            continue
        percent = math.ceil(x / y* 100)

        if percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        else:
            print(f"{percent:.0f}%")
        break

    except ValueError:
        continue
    except ZeroDivisionError:
        continue