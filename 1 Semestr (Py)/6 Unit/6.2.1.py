from random import *

arr =[]
n = int(input("Введите длину массива:"))

for i in range(0,n):
    arr.append(randint(-1000,1000))
fl = 0
maxx = - 1001
for i in arr:
    if abs(i) % 2 == 0:
        fl = 1
        if i > maxx:
           maxx = i          
if fl == 0:
    print("отсутствие искомых элементов")
else:
    print("Максимальные:",end="")
    for i in arr:
        if i == maxx:
            print(i,end=" ")
print()
k = 0
max_len = max(len(str(max(arr))), len(str(min(arr))))
for i in range(n):
    print(str(arr[i]).ljust(max_len), end=" ")
    k = k + 1
    if k % 5 == 0:
        print()
