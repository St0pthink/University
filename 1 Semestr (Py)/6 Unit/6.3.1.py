from random import *

arr =[]
n = int(input("Введите длину массива:"))

for i in range(0,n):
    arr.append(randint(-1000,1000))
print("Массив заданной размерности:" ,arr)

sm = 0
f = []
for i in arr:
    sm = sm + i
    f.append(sm)
print("Искомый массив: ",f)