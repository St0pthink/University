count = 0
summ = 1

while True:
    
    number = float(input("Введите число:"))
    if number > 10 and number <= 100:
        break
    summ = summ * number
    count = count + 1
answer  = summ**(1/count)
if count == 0:
    print("Среднее геометрическое не существует")
else: 
    print("Среднее геометрическое:{:.2f} ".format(answer))  
