from math import *


x = float(input("Введите значение x, не равное 0:"))
y = abs(sin((1+x**(1/3))/x))
print("Значение функции y в точке x={:.2f} равно {:.2f}".format(x,y))