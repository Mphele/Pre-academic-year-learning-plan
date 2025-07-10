def main():
    time  = input("Please enter a time: ")
    indicator = convert(time)
    if 7 <= indicator <= 8:
        print("breakfast time")
    elif 12 <= indicator <= 13:
        print("lunch time")
    elif 18 <= indicator <= 19:
        print("dinner time")

def convert(time):
    time = time.split(":")
    final = ""
    final += time[0]
    second = float(time[1])/60
    second = str(second)
    second = second.replace("0","")
    final += second
    return float(final)


if __name__ == "__main__":
    main()