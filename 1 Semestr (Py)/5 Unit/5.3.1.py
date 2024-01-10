number = int(input("Введите натуральное число для формулы:"))
i = 0
summ = 0    
for i in range(0,number):
    x = (-1)**i * (1/2**i)
    i = i + 1
    summ = summ + x
print("Результат формулы:{:.2f} ".format(summ))