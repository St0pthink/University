def main():
    lett = "AEIOUY"
    pr = []
    a = list(input("Введите строку: ").split())
    b = []
    for i in a:
        b.append(len(i))
    b = sorted(b)[::-1]
    len1 = b[0]
    len2 = b[1]
    c = 0
    for i in range(len(a)):
        if len(a[i]) == len1 or len(a[i]) == len2:
            c = c + 1
            for j in a[i]:
                if j in lett:
                    pr.append(j)
        if c == 2:
            break
    if pr == []:
        print("Искомые элементы  отсутствуют")
    else:
        print("Искомые элементы  присутсвуют")
        print("Символы: ", *set(pr))
main()