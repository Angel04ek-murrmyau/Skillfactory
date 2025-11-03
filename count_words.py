alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

eng_words = []
word_len_more_3 = []

filename = input("Введите название файла: ")


with open(filename + ".txt", "w", encoding="utf-8") as f:
    while True:
        fileinfo = input("Введите содержимое файла через пробел (чтобы выйти, напечатайте 'q'): ")
        if fileinfo.lower() == "q":
            break
        f.write(fileinfo + "\n")


with open(filename + ".txt", "r", encoding="utf-8") as f:
    text = f.read().split()


for word in text:
    if all(letter.lower() in alphabet for letter in word):
        eng_words.append(word)

if eng_words:
    longest_eng_word = max(eng_words, key=len)
else:
    longest_eng_word = "нет английских слов"


for word in text:
    if len(word) > 3:
        word_len_more_3.append(word)

if word_len_more_3:
    frequent_word = max(word_len_more_3, key=word_len_more_3.count)
else:
    frequent_word = "нет слов длиной > 3"


print("Самое длинное английское слово:", longest_eng_word)
print("Наиболее частое слово длиной > 3 символов:", frequent_word)










