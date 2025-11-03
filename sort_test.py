import datetime
import random

with open("replaces.txt", "a") as replaces:

    start_time = datetime.datetime.now()

    massiv = [random.randint(10,100) for i in range(10)]

    counter = 0
    for i in range(1, len(massiv)):
        b = massiv[i]
        j = i - 1
        while (j >= 0) and (b > massiv[j]):
            massiv[j + 1] = massiv[j]
            j -= 1
        massiv[j + 1] = b
        counter += 1

    end_time = datetime.datetime.now()
    replaces.write(str(counter) + " #insertion_sort \n")



