from random import randint
N = int(input("Введите ширину матрицы:"))
M = int(input("Введите длину матрицы:"))
ar = []

for i in range(N):
    ar.append([])
    for j in range(M):
        ar[i].append( randint (-999, 999))

maxx = 1
for i in range(N):
    for  j in range(0,M,2):
        if ar[i][j] < 0 and abs(ar[i][j]) % 9 == 0 and abs(ar[i][j]) % 16 == 0: 
            if ar[i][j] ==1 or ar[i][j] > maxx:
                maxx = ar[i][j]
if maxx == 1:
    print("Не существет")
else: 
    print("Максимальный отрицательный элемент среди элементов кратных 9 и 16:", maxx)
print(ar)