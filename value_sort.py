A = [2, 54, 38, 21, 10, 22, 45, 33]
result = []
f_half = A[:len(A) // 2]
s_half = A[len(A) // 2:]
for i in sorted(f_half), sorted(s_half):
    for j in i:
        result.append(j)
print(', '.join(str(el) for el in result))


