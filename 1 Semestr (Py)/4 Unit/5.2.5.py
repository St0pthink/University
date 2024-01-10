number = abs(int(input("Введите целое число:")))
flag = 0
while number != 0 :
    check = number % 10
    number = number // 10
    if check % 2 == 0:
        flag = 1
if flag == 1:
    print(" В числе есть цифры кратные 2")
else:
    print(" В числе нет цифр кратных 2")
