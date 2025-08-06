import emoji

user = input("Input: ")
words = user.split()

output = []

for word in words:
    cleaned = word.strip(":")
    alias = f":{cleaned}:"

    emojized = emoji.emojize(alias, language="alias")

    if emojized != alias:
        output.append(emojized)
    else:
        output.append(word)

print("Output:", " ".join(output))
