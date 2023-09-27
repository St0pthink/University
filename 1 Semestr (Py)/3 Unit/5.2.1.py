from math import *

x = float(input("Введите координату x:"))
y = float(input("Введите координату y:"))

if  y <= sin(x) and y >= 0 and y <= 0.5:
    if y == sin(x) or y == 0 or y == 0.5:
        print("На границе")
    else:
        print("Да")
else:
        print("Нет")