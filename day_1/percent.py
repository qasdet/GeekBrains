#for i in range(150):
i = 1
while i < 150:
    i += 1
    n_str = str(i + 1)
    n_list = list(n_str)
    if int(n_list[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    elif int(n_list[-1]) > 1 and int(n_list[-1]) <= 4:
        if i + 1 > 10 and i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))
print('Задание №2 - Склонение слова - Процент')