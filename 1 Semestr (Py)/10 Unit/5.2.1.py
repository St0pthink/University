from math import *

def drob(x):
 if x<5: return "Не существует"
 elif 5<=x<9: return (1/(cos(sin(x-2))))
def mlog(x):
 if 9<=x<17: return (2* 5**x - 4*log(x**2,8))
def trig(x):
 if 17<=x<=22: return cos(x**3 - 2*x + 3)/sin(x**3 - 2*x + 3)
 else: return "Не существует"
def fprint(v="X", s="Y"):
 print("{:10}|{:15}".format(v,s))
def main():
 fprint()
 for i in range(5,23):
    if i<9:
        fprint(i,drob(i))
    elif 9<=i<17:
        fprint(i,mlog(i))
    else:
        fprint(i,trig(i))

main() 