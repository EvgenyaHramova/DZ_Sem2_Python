# Реализуйте алгоритм перемешивания списка.

import random

ran = range(-5, 6)
numbers = list(ran)
print(f'Сгенерирован список: {numbers}')

random.shuffle(numbers)
print(f'\nСписок после перемешивания: {numbers}')
