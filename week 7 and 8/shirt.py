from PIL import Image,ImageOps
import sys
from pathlib import Path

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

before_image = sys.argv[1]
after_image = sys.argv[2]

before_path = Path(sys.argv[1])
after_path = Path(sys.argv[2])

valid_types = [".jpg", ".jpeg", ".png"]
if not any(before_image.lower().endswith(ext) for ext in valid_types):
    sys.exit("Invalid input file extension")
if not any(after_image.lower().endswith(ext) for ext in valid_types):
    sys.exit("Invalid output")

if before_path.suffix.lower() != after_path.suffix.lower():
    sys.exit("Input and output must have the same extension")

if not before_path.exists():
    sys.exit(f"Input does not exist")

try:
    with Image.open(before_image) as before, Image.open("shirt.png") as shirt:
        img = ImageOps.fit(before, shirt.size)
        img.paste(shirt,(0,0), shirt)
        img.save(after_image)
except FileNotFoundError:
    sys.exit("shirt.png not found")