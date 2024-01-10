#задание массива для сортировки
from random import *
from datetime import datetime
ar10000 =[]
#задания массива случайными числами
for i in range(0,10000):
    ar10000.append(randint(-1000,1000))

arr = ar10000.copy() 
start_time = datetime.now()
#bubble sort (сортировка пузырьком)

n = len(arr)
count = 0
x = 0
    #пробеги до момента сортировки
while True:
    fl = 0
    for i in range(1,n - x):
        if arr[i-1] > arr[i]:
            #перестановка большего на меньшее
            arr[i-1], arr[i] = arr[i], arr[i-1]
            count = count + 1
            fl = 1
    x = x + 1
    if fl == 0:
        break  
end_time = datetime.now()
print('Время выполнения пузырьком: {},'.format(end_time - start_time),"количество перестановок: {}.".format(count))

arr = ar10000.copy() 
start_time = datetime.now()
#selection sort (сортировка выбором)

count = 0
n = len(arr)
for i in range(n):
    minn = i
    for j in range(i+1,n):
        # Выбор наименьшего значения
        if arr[j] < arr[minn]:
            minn = j
    # Помещаем это перед отсортированным концом массива
    if i != minn:
        arr[minn], arr[i] = arr[i], arr[minn]
        count = count + 1
end_time = datetime.now()
print('Время выполнения выбором: {},'.format(end_time - start_time),"количество перестановок: {}.".format(count))

arr = ar10000.copy() 
start_time = datetime.now()
#insertion Sort(сортировка вставками)


count = 0
for i in range(len(arr)):
    cursor = arr[i]
    pos = i
    while pos > 0 and arr[pos - 1] > cursor:
        # Меняем местами число, продвигая по списку
        arr[pos] = arr[pos - 1]
        count = count + 1
        pos = pos - 1
    # Остановимся и сделаем последний обмен
    arr[pos] = cursor
    count = count + 1
end_time = datetime.now()
print('Время выполнения вставкой: {},'.format(end_time - start_time),"количество перестановок: {}.".format(count))