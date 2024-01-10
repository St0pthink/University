def young(v):
 if v<=0: return "Нет такого возраста"
 elif 0<v<=17: return "Несовершеннолетний"
 else: return "Совершеннолетний"
def average(v):
 if v<=50: return "В полном расцвете сил"
 else: return "Все еще замечательно"
def adult(v):
 if v<=90: return "Как хорошо на свете жить"
 elif 90<v<=120: return "Покой нам только снится"
 else: return "Все еще впереди"
def fprint(v="Возраст", s="Сообщение"):
 print("{:10}|{:15}".format(v,s))
def main():
 fprint()
 for i in range(151):
    if i<30:
        fprint(i,young(i))
    elif 30<=i<65:
        fprint(i,average(i))
    else:
        fprint(i,adult(i))

main() 