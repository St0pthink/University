def main():
    a = list(input("Введите строчку:").split())
    c = 0
    for i in a:
        if len(i) == 5:           
            c = c + 1
    if c == 0:
        print ("Искомые элементы отсутствуют")
    else:
        print("Искомые элементы присутствуют")
    print("Количество слов длиной 5 символов:", c)
main()
