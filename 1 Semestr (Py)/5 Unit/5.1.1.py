from math import *

border1 = int(input("Введите 1 границу:"))
border2 = int(input("Введите 2 границу:"))

if border1 > border2:
    border2, border1 = border1,border2
summ = 0
for i in range(border1,border2+1):
    if i % 5 != 0:
        summ = summ + cos(i)
if border1 == border2 and border1 % 5 == 0:
    print("Не существует")
print("Сумма косинусов:{:.2f} ".format(summ))  