import json
import os

# Drill 1 - Python to JSON text and back
data = [{"name": "Miraan", "learning": True}]
text = json.dumps(data)
print(text)
print(type(text))

back = json.loads(text)
print(back)
print(type(back))

# Drill 2 - writing to a file
with open("drill.json", "w") as f:
    json.dump(data, f, indent=2)
print("written")

# Drill 3 - reading it back
with open("drill.json", "r") as f:
    loaded = json.load(f)
print(loaded)
print(loaded[0]["name"])

# Drill 4 - checking a file exists
print(os.path.exists("drill.json"))
print(os.path.exists("nothing_here.json"))
