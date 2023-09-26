from math import *


x = int(input("Введите число, не равное 0:"))
y = abs(sin((1+x**(1/3))/x))
print("Значение функции y в точке x={:.2f} равно {:.2f}".format(x,y))