import csv
import random
def main():
    ru_alphabet = "ЁЙЦУКЕНГШЩЗЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    with open('data.csv', 'w', encoding="utf8") as csvfile:  #для обнуления файла
        pass
    while True:
        print ("1 - Запись в файл вручную")
        print ("2 - Запись в файл генерацией")
        print ("3 - Ввывод файла")
        print ("4 - Вывести на экран всех студентов чеё балл больше 4.0")
        print()
        put = input("Введите число, соответствующее функции: ")
        if put == "1":
                lastname,intitials = input ( "Введите Фамилию и инициалы (c точкой) через пробелы: ").split(None ,1)
                group = input ( "Введите номер группы: ")
                grade1, grade2, grade3, grade4, grade5  = input( "Введите оценки через пробелы: ").split()
                with open('data.csv', 'a', encoding="utf8") as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([lastname,intitials,group,grade1,grade2,grade3,grade4,grade5]) 
        if put == "2": #генерация
            n = int(input("Сколько данных студентов хотите сгенерировать:"))
            k = int(input("Сколько всего групп:"))
            for _ in range(n):
                with open("last_names.txt",encoding="utf-8") as f: #Список Фамилий
                    rand_names = f.readlines()
                    lastname = (rand_names[random.randint(0,len(rand_names)-1)])[:-1]
                intitials = ru_alphabet[random.randint(0,len(ru_alphabet)-1)] + ". " + ru_alphabet[random.randint(0,len(ru_alphabet)-1)] + "."
                group =  random.randint(1,k)
                grade1 = random.randint(1,5)
                grade2 = random.randint(1,5)
                grade3 = random.randint(1,5)
                grade4 = random.randint(1,5)
                grade5 = random.randint(1,5)
                with open('data.csv', 'a', encoding="utf8") as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([lastname,intitials,group,grade1,grade2,grade3,grade4,grade5]) 
        if put == "3":
                with open('data.csv', encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                    
                    for row in reader:
                        if row == []:
                                pass
                        else:print("Фамилия:",row[0],row[1], "Группа:", row[2], "Оценки:", row[3],row[4],row[5],row[6],row[7])
                    print()
        if put == "4":
            with open('data.csv', encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                    fl = 0
                    for row in reader:
                        if row == []:
                            pass
                        elif (int(row[3]) + int(row[4]) + int(row[5]) + int(row[6]) + int(row[7])) / 5 > 4:
                            fl = 1
                            print("Фамилия: ",row[0], " Группа: ", row[2])
                    if fl == 0:
                         print("Отсутствют студенты со среднем баллом больше 4") 
                    print()

main()