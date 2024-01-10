def main():
    a = input("Введите строчку: ") 
    fl = 1
    b = ""
    for i in range(int(len(a)/2)):
        if a[i] == "g":
            fl = 0
            b = b + "*"
        else:
            b = b + a[i] 
    if fl == 1:
        print ("Искомые элементы отсутствуют")
    else:
        print ("Искомые элементы присутствуют")
    a = b + a[int(len(a)/2):]
    print("Итоговая строка:",a)

main()
