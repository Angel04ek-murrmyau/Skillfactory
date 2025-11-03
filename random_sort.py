from random import randint

lst = [randint(-1000,1000) for i in range(100)]
print(sorted(lst))
print(sorted(lst, reverse=True))
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
