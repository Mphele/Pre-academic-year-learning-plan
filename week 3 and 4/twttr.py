#Remove all vowels 

vowels ="aeiouAEIOU"
final_tweet =""
user_input=input("Enter your tweet: ")
#Where is my ball? 
for char in user_input:
    if char in vowels:
        continue
    final_tweet+=char
    print(final_tweet)

print(final_tweet)

