accuracy = float(input("Введите точность последовательности:"))
delimoe = 1
delitel = 1 
n = 1
number =  delimoe / delitel
summ = number
if number <= accuracy:
    print("Сумма ряда: 0")
while True:
    n = n + 1
    delimoe = delimoe * n
    delitel = n**n
    number = delimoe / delitel
    if number <= accuracy:
        break
    summ = summ + number
print("Сумма ряда:{:.10f} ".format(summ))   