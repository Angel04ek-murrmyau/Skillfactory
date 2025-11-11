import json

with open("text.json") as f:
    data = json.load(f)
    data = data.lower()
with open("text.json","w") as f:
    json.dump(data, f)
