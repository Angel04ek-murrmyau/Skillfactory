import json

with open("array.json") as f:
    file_content = f.read()
    data = json.loads(file_content)
    new_data = [i + data.index(i) for i in data]

with open("array.json", "w") as f:
    json.dump(new_data, f)
