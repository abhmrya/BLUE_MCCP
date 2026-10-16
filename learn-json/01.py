import json

from pathlib import Path

file_path = Path("learn-json/01.json")

with file_path.open('r',encoding='utf-8') as file:
    print(file)
    product = json.load(file)

print(product["id"])
print(product["rating"]["rate"])