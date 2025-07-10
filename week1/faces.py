def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

def main():
    string = input("Please enter a sentence: ")
    print(convert(string))

main()
