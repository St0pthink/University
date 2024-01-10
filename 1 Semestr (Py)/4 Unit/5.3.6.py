accuracy = float(input("Введите точность последовательности:"))
delimoe = 2
delitel = 1 * 2 * 3
n = 1
number =  delimoe / delitel
summ = number
if number <= accuracy:
    print("Сумма ряда: 0")
while True:
    n = n + 1
    delimoe = delimoe * 2
    delitel = delitel * (n*2) * ((n*2)+1) * (n*3)
    number = delimoe / delitel
    if number <= accuracy:
        break
    summ = summ + number
print("Сумма ряда:{:.10f} ".format(summ))  