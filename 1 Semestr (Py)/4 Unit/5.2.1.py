number = abs(int(input("Введите целое число:")))
n = (int(input("Введите  число n:")))
flag = 0
while number != 0 :
    check = number % 10
    number = number // 10
    if check == n:
        flag = 1
if flag == 1:
    print(" В числе есть цифра n")
else:
    print(" В числе нет цифы n")