from math import *

def h(a,b, angle):
    hb = b *sin(angle)
    ha = a *sin(angle)
    c = (a**2 + b**2 - 2*b*a*cos(angle))**(1/2)
    S = a*b*sin(angle)*(1/2)
    hc = (S * 2) / c
    return ha,hb,hc

a = int(input("Введите первую сторону треугольника:"))
b = int(input("Введите вторую сторону треугольника:"))
angle = int(input("Введите угол между сторонами треугольника:"))
    
print("Высоты для заданного треугольника:",h(a,b,angle))