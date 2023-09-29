from math import *

a = float(input("Введите большее основание трапеции:"))
b = float(input("Введите меньшее основание трапеции:"))
angle = float(input("Введите угол при большем основании(от 1 до 89 включительно):"))
h = (sin(angle)/cos(angle)) *( abs(a-b) / 2)
S = h * (a+b) / 2
print("площадь равнобедренной трапеции:{:.2f} ".format(S))
