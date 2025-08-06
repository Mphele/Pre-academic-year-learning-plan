import random
import sys
import pyfiglet

if len(sys.argv)==1:
    random_font = random.choice(pyfiglet.FigletFont.getFonts())
    user = input("Input: ")
    figgy = pyfiglet.figlet_format(user,font=random_font )
    print(figgy)
elif len(sys.argv)==3 and sys.argv[1]==("-f" or "--font"):
    user = input("Input: ")
    figgy = pyfiglet.figlet_format(user, font=sys.argv[2])
    print(figgy)
else:
    # print("Invalid usage")
    sys.exit("Invalid usage")