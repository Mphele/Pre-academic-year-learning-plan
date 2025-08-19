import csv
from sys import argv
from sys import exit
from pathlib import Path
from tabulate import tabulate
if len(argv)>2:
    exit("Too many command-line arguments")
if len(argv)<2:
    exit("Too few command-line arguments")
if not argv[1].endswith(".csv"):
    exit("Not a CSV file")
if not Path(argv[1]).exists():
    exit("File does not exist")
if argv[1] == "regular.csv":
    with open("regular.csv", "r") as reg:
        reader = csv.DictReader(reg)
        full_data = list(reader)
        print(tabulate(full_data, headers="keys",tablefmt="grid" ))

elif argv[1]=="sicilian.csv":
    with open("sicilian.csv", "r") as reg:
        reader = csv.DictReader(reg)
        full_data = list(reader)
        print(tabulate(full_data, headers="keys",tablefmt="grid" ))

