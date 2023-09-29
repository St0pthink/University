
r = float(input("Введите значение(>0) r:"))
x = float(input("Введите координату x:"))
if x < -(r+5):
    y = -r
    print("Значение функции y равно {:.2f} ".format(y))
elif x >= -(r+5) and x < -r:
    t = r/5
    y = (t*r) +(t*x) 
    print("Значение функции y равно {:.2f} ".format(y))
elif x >= -r and x < r:
    y = -((r**2 - x**2)**(1/2))
    print("Значение функции y равно {:.2f} ".format(y))    
elif x >= r and x <= r+2:
    y = x - r
    print("Значение функции y равно {:.2f} ".format(y))  
else:
    y = 3
    print("Значение функции y равно {:.2f} ".format(y))  