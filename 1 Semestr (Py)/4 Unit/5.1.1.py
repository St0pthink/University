count = 0
minn =  float(input("Введите число:"))
number = minn
while True:
    if number >= -10 and number <= -1:
        break
    count = count + 1
    if number < minn:
        minn = number 
    number = float(input("Введите число:"))
   
print("Количество:{:.2f} ".format(count))
if count == 0:
    print("Минимальное не существует")
else:  
    print("Минимальное:{:.2f} ".format(minn))  