# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Введите число N = ')
n = int(input())
result = 1
print('тогда ', end='[ ')
for i in range(1, n):
    result = result * i
    print(result, end=', ')
print(result*n, end=' ]')
