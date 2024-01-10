def create_list():
    ar = list(map(int,input("Введите массив:").split()))
    return ar


def main():    
    ar = create_list()
    while True:
        print ("1 - Вывод массива на экран")
        print ("2 - Редактирование i элемента массив")
        print ("3 - Вычислить среднее арифметическое положительных элементов массива")
        print ("4 - Вывести элементы массива кратные 4 на экран в обратном порядке.")
        print ("5 - Отсортировать массив методом выбора элементов и вывести отсортированный массив на экран")
        print()
        put =  input("Введите число, соответствующее функции:")
        if put == "1":
            print(*ar)
            print()
        if put == "2":
            k = int(input("Введите номер элемента массива (счёт с 1):")) 
            n = int(input("Введите число для замены:"))
            ar[k-1] = n
            print()
        if put == "3":
            count = 0
            sm = 0
            for k in ar:
                    if k > 0:
                        count = count + 1
                        sm = sm + k
            t1 = sm/count
            if count > 0:
                print ("Искомые элементы присутствуют")
                print ("Cреднее арифметическое положительных элементов массива:",t1)
            else:
                print ("Отсутствие искомых элементов")
            print()
        if put == "4":
            temp_list = []
            arr = ar[::-1]
            for  i in arr:
                if  i % 4 == 0:
                    temp_list.append(i)
            if temp_list == []:
                print ("Отсутствие искомых элементов")
            else:
                print ("Искомые элементы присутствуют")
                print ("Элементы массива кратные 4 на экран в обратном порядке:")
                print(*temp_list)
            print()

        if put == "5":
            count = 0
            n = len(ar)
            for i in range(n):
                minn = i
                for j in range(i+1,n):
                    # Выбор наименьшего значения
                    if ar[j] < ar[minn]:
                        minn = j
                # Помещаем это перед отсортированным концом массива
                if i != minn:
                    ar[minn], ar[i] = ar[i], ar[minn]
            print(*ar)
            print()

main()
