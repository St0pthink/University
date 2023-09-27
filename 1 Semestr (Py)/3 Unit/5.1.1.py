from math import *


a = float(input("Введите число a:"))
b = float(input("Введите число a:"))
c = float(input("Введите число a:"))
x = float(input("Введите число a:"))


if x < 0 and b != 0:
    if a == 0:
        print("Значение функции F не вычисляется")
    else:
        F = ((-(-x)**(1/3)) + b) // a
        print("Значение функции F равно {:.2f} ".format(F))
elif x > 0 and b > 0:
    if 3*x - b*c == 0:
        print("Значение функции F не вычисляется")
    else:
        F = (x**2 - sin(a-2)) /(3*x - b*c)
        print("Значение функции F равно {:.2f} ".format(F))
else:
    if x <= 0 or c == 0:
        print("Значение функции F не вычисляется")
    else:
        F = log(x) / c
        print("Значение функции F равно {:.2f} ".format(F))