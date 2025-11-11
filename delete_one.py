def delete_one(string):
    line = string.lower().split()
    counter = {}
    for word in line:
        counter[word] = counter.get(word, 0) + 1
    filtered_line = [word for word in line if counter[word] > 1]
    result = " ".join(filtered_line)
    print(result)

delete_one("Python простота и универсальность python делают его одним из лучших языков программирования.")
