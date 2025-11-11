with open("pallindroms.txt", "r", encoding="utf-8") as f:
    pallindroms = []
    text = f.read()
    text = text.split()
    for word in text:
        if word == word[::-1]:
            pallindroms.append(word)
    print(pallindroms)