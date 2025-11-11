counter = {"a": 2, "b": 4, "c": 3}
count = 4

for k, v in counter.items():
    if v == count:
        most_frequent = k
        break
print(most_frequent)


