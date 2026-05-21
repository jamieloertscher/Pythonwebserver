import os

filepath = "/data/data.txt"

if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"Datei nicht gefunden unter {filepath}")