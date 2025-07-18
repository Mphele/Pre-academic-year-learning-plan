answer = input("Please enter a greeting: ").lower()
final = answer.replace(" ", "")

if "hello" in final:
    print("$0")
elif final[0] == "h":
    print("$20")
else:
    print("$100")