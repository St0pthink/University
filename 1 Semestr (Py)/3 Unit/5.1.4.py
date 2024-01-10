from math import *


a = float(input("Введите число a:"))
b = float(input("Введите число b:"))
c = float(input("Введите число c:"))
x = float(input("Введите число x:"))


if x < 0 and b != 0:
    if b - 1 == 0:
        print("Значение функции F не вычисляется")
    else:
        if 1 - x < 0:
            F = ((-(x-1)**(1/3)) + c) // b-1
            print("Значение функции F равно {:.2f} ".format(F))
        else:
            F = (((1-x)**(1/3)) + c) // b-1
            print("Значение функции F равно {:.2f} ".format(F))
elif x > 0 and b > 0:
    if 8*(x**5) + c == 0:
        print("Значение функции F не вычисляется")
    else:
        F = (cos(a*x - b)) / (8*(x**5) + c)
        print("Значение функции F равно {:.2f} ".format(F))
else:
    if cos(x) == 0 or (c+5)**4 == 0:
        print("Значение функции F не вычисляется")
    else:
        F = (sin(x)/cos(x)) / c
        print("Значение функции F равно {:.2f} ".format(F))