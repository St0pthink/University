def summ(n, sm = 0,fc = 1, i = 1,):
    fc = fc * i
    t = fc / (2*i +  2)
    if i == n:
        return sm + t
    return summ(n, sm + t,fc,i + 1)
    


def main():
    n = int(input("До какого элемениа считаем сумму:"))
    print("Cумма: ", summ(n))
main()