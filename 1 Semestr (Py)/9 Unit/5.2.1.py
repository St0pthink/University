from random import randint
N = int(input("Введите ширину матрицы:"))
M = int(input("Введите длину матрицы:"))
ar = []

for i in range(N):
    ar.append([])
    for j in range(M):
        ar[i].append( randint (-999, 999))

mdg = 1
count = 0
fl = 1
for i in range(0,N,2):
    for  j in range(1,M,2):
        if ar[i][j] > 0 and ar[i][j] % 7 == 0:
            mdg = mdg * ar[i][j]
            count = count + 1
            fl = 0
if fl == 1 :
    print("Среднего геометрического не существует")
else:
    fl = 1
    x = mdg**(1/count)
    for i in range(N):
        for  j in range(M):
            if ar[i][j] > x :
                fl = 0
                print("Элемент:",ar[i][j], "с индексом",i,"и",j)
    if fl == 1:
        print("Не существует подходящих элементов")
print(ar)