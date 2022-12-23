# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Вариант для целых чисел
# print('Введите число:')
# num = int(input())
# num = abs(num)
# summa = 0
# while num != 0:
#     summa += (num % 10)
#     num //= 10
# print('Сумма цифр в числе составляет: ', summa)


print('Введите число:')
num = input()
summa = 0
for num_str in num:
    if num_str != '.':
        summa += int(num_str)
print('Сумма цифр в числе составляет: ', summa)
