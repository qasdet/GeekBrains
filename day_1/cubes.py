print('Задание №3 Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело')
number = 0
sum = 0
sums = 0
while number <= 1000:
    number += 1
    cubes = number ** 3
    sum = sum + cubes % 10
    num = cubes
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
        if not number % 2 == 0 and sum == 28:
            sums += number
            print(f"Целое  число: {number} | Куб: {cubes} | Сумма числа |{number} | {sums} равна: [{sum}]")
