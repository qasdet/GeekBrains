t = int((input("Введите значение: ")))
d, h, m, s, = t // 86400, t // 25200, t // 60 % 60, t % 60
print(f'{d} дн, {h} час, {m} мин, {s} cек')
print('Задание №1 - Вывод времени в формате - день, часы, минуты, секунды')