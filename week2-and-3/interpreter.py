sum = input("Expression: ").replace(" ", "")

if "+" in sum:
    sum = sum.split("+")
    print(float(sum[0])+float(sum[1]))
elif "-" in sum:
    sum = sum.split("-")
    print(float(sum[0])-float(sum[1]))
elif "*" in sum:
    sum = sum.split("*")
    print(float(sum[0])*float(sum[1]))
elif "/" in sum:
    sum = sum.split("/")
    print(float(sum[0])/float(sum[1]))

