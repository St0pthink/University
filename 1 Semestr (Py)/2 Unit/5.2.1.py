number = int(input("трехзначное число:"))
first =  (number - (number % 100))// 100
second = (number % 100 - number % 10)//10
third =  number % 10
print (number == first**3 + second**3 + third**3)