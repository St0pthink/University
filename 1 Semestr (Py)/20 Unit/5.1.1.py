def main():
    pull_1 = list(map(int,input("Введите 1 множество: ").split()))
    pull_2 = list(map(int,input("Введите 2 множество: ").split()))
    print_list = list(map(lambda x,y: x+y,pull_1,pull_2))
    print("Cписок сумм попарных элементов: ", *print_list)
main()