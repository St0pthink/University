from random import randint
N = int(input("Введите ширину матрицы:"))
M = int(input("Введите длину матрицы:"))
ar = []

for i in range(N):
    ar.append([])
    for j in range(M):
        ar[i].append( randint (-999, 999))
print("Двумерный массив заданной размерности:" ,ar)
A = int(input("Введите число A:"))
f = []
for i in range(N):
    count = 0
    for j in ar[i]:
        if j > A:
            count = count + 1
    f.append(count)
print("Искомый одномерный массив: ",f)