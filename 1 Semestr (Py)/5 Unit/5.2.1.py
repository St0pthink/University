number = int(input("Введите натуральное число для возведение в квадрат:"))
x = 1
summ = 0
for i in range(1,number+1):
    summ = summ + x
    x = x + 2
print("Квадрат числа:{:.2f} ".format(summ))  