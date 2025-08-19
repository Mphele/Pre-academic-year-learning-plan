from sys import argv
from sys import exit
from pathlib import Path
if len(argv)>2:
    exit("Too many command-line arguments")
if len(argv)<2:
    exit("Too few command-line arguments")
if not argv[1].endswith(".py"):
    exit("Not a python file")
if not Path(argv[1]).exists():
    exit("File does not exist")

with open(argv[1], "r") as file:
    counter =0
    for row in file:
        if row.lstrip().startswith("#") or row.strip()=="":
            continue
        counter+=1

print(counter)