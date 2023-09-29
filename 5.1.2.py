from math import *


x = float(input("Введите значение x:"))
t = float(input("Введите значение t, не равное 2*Pi*n, n - любое целое:"))
f = (1 + x**2 - 2*x*t)/ sin(t) + 1 + sqrt(1 + sin(x)**2 + cos(x*t)**2)
print("Значение функции f(x;t) в точке x= {:.2f} и в точке t = {:.2f} равно {:.2f}".format(x,t,f))