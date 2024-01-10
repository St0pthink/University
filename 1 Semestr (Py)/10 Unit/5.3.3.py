from math import *

def g(a,b):
    g = ((a**2 - b**2)/ (2*a*b - a - b)) + ((a+b) * (abs(a+b)/2)**(1/2))
    return g
def f(s,t):
    f = g(1.2, s) + g(t,s) - g(2*s-1, s*t)
    return f
s = int(input("Введите значение s:"))
t = int(input("Введите значение t:"))
print("Значение выражения: ",f(s,t))