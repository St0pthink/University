import csv


def open_dict(): #считываем глосарий с файла
    with open('bible.csv', encoding="utf8") as csvfile:
        dict_main  = {}
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for index, row in reader:
            dict_main[index] = row
    return dict_main  


def save_file(dict_main): # сохранение глоссария в файл
    with open('bible.csv', 'w', encoding="utf8",newline="") as csvfile:
                        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for index, row in dict_main.items():
                            if index  == "":
                                pass
                            else:
                                writer.writerow([index,row])


def add_dict(dict_main): #дополнение голосария
    term = input("Введите термин: ")
    mean = input("Введите значение термина: ")
    dict_main[term] = mean


def del_dict(dict_main): #удаление по термину
    term = input("Введите термин, который хотите удалить: ")
    try: 
        del dict_main[term]
    except KeyError:
        print ("Такого термина нет в голосарии")


def print_dict(dict_main): #вывод глоссария
    for key,value in dict_main.items():
        print(key + " : "+ value.replace("\\n","\n"))


def find_dict (dict_main): #поиск по термину
    term = input("Введите термин, который хотите найти: ")
    try: 
        print (dict_main[term])
    except KeyError:
        print ("Такого термина нет в голосарии")


def main():
    while True:
        print ("1 - Cоздание глоссария")
        print ("2 - Cохранение глоссария в файл")
        print ("3 - Дополнение глоссария парами - термин : толкование термина")
        print ("4 - Удаление из глоссария пар - термин : толкование термина")
        print ("5 - Вывод глоссария на экран")
        print ("6 - Поиск в глоссарии толкования термина и вывод его на экран.")
        put = input("Введите число, соответствующее функции: ")
        if put == "1":
            dict_main = open_dict()     
        if put == "2":
            try: 
                save_file(dict_main)
            except NameError:
                print("Не создан глосарий")
                continue
        if put == "3":
            try: 
                add_dict(dict_main)
            except NameError:
                print("Не создан глосарий")
                continue
        if put == "4":
            try: 
                del_dict(dict_main)
            except NameError:
                print("Не создан глосарий")
                continue
        if put == "5":
            try: 
                print_dict(dict_main)
            except NameError:
                print("Не создан глосарий")
                continue
        if put == "6":
            try: 
                find_dict(dict_main)
            except NameError:
                print("Не создан глосарий")
                continue




main()