import json

with open('text2.json') as f:
    text = json.load(f)

line = text.split()
counter = {}
for word in line:
    counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]

while most_frequent[0] in line:
    i = line.index(most_frequent[0])
    line.remove(most_frequent[0])
    
with open('text2.json', 'w') as f:
    json.dump(" ".join(line), f)
