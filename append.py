import random

def merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c

print(merge(a = sorted([random.randint(1, 100) for i in range(3)]), b = sorted([random.randint(1, 100) for i in range(3)])))
