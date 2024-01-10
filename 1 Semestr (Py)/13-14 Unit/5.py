from random import *
import pprint

def make_ar(i,j):
    ar = [0]*j
    for k in range(j):
       ar[k]=[randint(-1000,1000)  for n in range(i)]
    return ar


def task1(ar,i,j):
    count = 0
    sm = 0
    for k in range(j):
        for n in range(i):
            if ar[k][n] % 2 == 0:
                count = count + 1
                sm = sm + ar[k][n]
    if count > 0:
        return (sm/count,bool(count))
    else:
        return (0, bool(count))


def task2(ar,i,j):
    maxx = 1
    for k in range(1,j,2):
        for n in range(0,i,2):
            if ar[k][n] % 3 == 0:
                if maxx==1 or ar[k][n] > maxx == 0:
                    maxx = ar[k][n]
    if maxx == 1 :
        print("Искомого элемента не существует")
    else:
        print("Искомый элемент:", maxx) 
        fl = 0
        for k in range(j):
            for  n in range(i):
                if ar[k][n] > maxx:
                    fl = 1
                    print ("Элемент: ",ar[k][n], " Индекс: [",k,",", n,"]",sep="")
        if fl == 0:
            print("Не существует подходящих элементов")

        



def main():    
    i = int(input("Количество столбцов:"))
    j = int(input("Количество строк:"))
    ar = make_ar(i,j)
    while True:
        print ("1 - вывод многомерного массива на экран")
        print ("2 - редактирование i,j элемента массив")
        print ("3 - вычислить среднее арифметическое четных элементов двухмерного массива")
        print ("4 - вывести на экран все элементы массива большие найденного максимального и их индексы")
        print()
        put =  input("Введите число, соответствующее функции:")
        if put == "1":
            pprint.pprint(ar)
            print()
        if put == "2":
            it,jt = map(int,input("Введите координату числа редактирования:").split())
            n = int(input("Введите число для замены:"))
            ar[it][jt] = n
            print()
        if put == "3":
            ma, bl = task1(ar,i,j)
            if bl == 0:
                print ("Отсутствие искомых элементов")
                print (bl)
                print()
            else:
                print ("Искомые элементы присутствуют")
                print(ma,bl)
                print()
        if put == "4":
            task2 (ar,i,j)
            print()

main()
