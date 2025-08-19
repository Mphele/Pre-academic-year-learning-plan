import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

combined = []
i=0
with open("before.csv", "r") as file, open("after.csv","w") as final:
    reader = csv.DictReader(file)
    writer = csv.DictWriter(final, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
      combined.append(row['name'].split(","))
      combined[i].extend([row['house']])
      writer.writerow({"first":combined[i][1].strip(), "last":combined[i][0].strip(), "house":combined[i][2].strip()})
      i+=1

