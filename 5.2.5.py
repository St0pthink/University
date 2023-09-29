number = int(input("четырехзначное положительное число:"))
first =  (number//1000) % 10
second = (number//100) % 10
third = (number//10) % 10
forth =  number % 10
print ( (first% 3 == 0)or(second% 3 == 0)or(third% 3 == 0)or(forth% 3 == 0))