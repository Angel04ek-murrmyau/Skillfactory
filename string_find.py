word = "one"    
strings = {"string_1": "one two one three one five", "string_2": "one four two", "string_3": "one nine one two"}
mass = []
counter = {}

for i,j in strings.items():
    if word in j:
        mass.append((i,j))
for i in mass:
  counter[i[1]] = i[1].count(word)
  max_count = max(counter.values())
  most_frequent = [k for k, v in counter.items() if v == max_count]

print(most_frequent[0])

