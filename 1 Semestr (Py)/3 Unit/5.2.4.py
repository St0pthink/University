from math import *

x = float(input("Введите координату x:"))
y = float(input("Введите координату y:"))

if  (x <= 1 and y >= 1 - x)and (y >= 2*(x**2) or x >= 0):
    if x == 1 or (y == 1 - x and x >= -1) or (y == 2*(x**2) and x <= -1):
        print("На границе")
    else:
        print("Да")
else:
        print("Нет")