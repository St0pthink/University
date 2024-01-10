from random import *

arr =[]
n = int(input("Введите длину массива:"))

for i in range(0,n):
    arr.append(randint(-1000,1000))
proizvodnoe = 1
fl = 0
count = 0
for i in arr:
    if (i % 5 == 0 or i % 7 == 0) and i > 0:
        fl = 1
        proizvodnoe = proizvodnoe * i
        count = count + 1
if fl == 0:
    print("отсутствие искомых элементов")
else:
    answer =  proizvodnoe**(1/count)
    print("Среднее геометрическое:{:.2f} ".format(answer))
k = 0
max_len = max(len(str(max(arr))), len(str(min(arr))))
for i in range(n):
    print(str(arr[i]).ljust(max_len), end=" ")
    k = k + 1
    if k % 5 == 0:
        print()