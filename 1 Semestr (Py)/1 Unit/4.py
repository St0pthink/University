print ('Вычесление дохода по вкладу.')
print('Введите исходные данные:')
sum = int(input( "величина вклада (руб.) - > "))
day = int(input( "срок вклада (дней) - > "))
procent = int(input("процентная ставка  (годовых) - > "))
print('//////////////')
profit = procent/36500 * day * sum
print("Доход: {:.2f} руб.".format(profit))
sum_profit = sum + profit
print("Сумма по окончании срока вклада: {:.2f} руб.".format(sum_profit))