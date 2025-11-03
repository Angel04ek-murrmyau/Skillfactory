def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input('Введите число: '))
row = []
for i in range(num + 1):
    row.append(factorial(i)) if i % 2 == 0 else 0

print(f"Сумма всех цифр факториала стоящих на нечетной позиции длиной {num} равна {sum(row)}")

