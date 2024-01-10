from string import ascii_lowercase #строчный английсский алфавит


def main():
    str1 = set(input("Введите 1 строчку: "))
    str2 = set(input("Введите 2 строчку: "))
    print("Общие символы:")
    for i in ascii_lowercase:
        if i in str1 and i in str2:
            print(i,end="")
main()