from math import *

def summ(n, sm = 0,fc = 24, i = 1,):
    fc = fc * (i + 4)
    t = log(i+1) / fc
    if t < n:
        return sm
    return summ(n, sm + t,fc,i + 1)
    


def main():
    
    n = float(input("С какой точностью считаем сумму ряда:"))
    print(summ(n))
main()
