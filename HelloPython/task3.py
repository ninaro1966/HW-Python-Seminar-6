#3. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.
# Получилась задача с list comprehansion
import random

NumberN = int(input('Введите длинну списка чисел N: '))

my_result = [random.randint(-NumberN, NumberN) for _ in range(NumberN)]


print(f'Случайная последовательность чисел: {my_result}')
path = r'file.txt'
with open("file.txt", 'r') as data:
    coef1 = data.readline()[:-1]
    coef2 = data.readline()
print(f'Сомножители на позициях')
print(coef1, end=' и ')
print(coef2, end=' дают результат: ')

print(my_result[int(coef1)]*(my_result[int(coef2)]))
# Изначальный вариант
# import random
#
# NumberN = int(input('Введите длинну списка чисел N: '))
#
# result = []
#
# for _ in range(NumberN):
#     result.append(random.randint(-NumberN, NumberN))
#
# print(f'Случайная последовательность чисел: {result}')
# path = r'file.txt'
# with open("file.txt", 'r') as data:
#     coef1 = data.readline()[:-1]
#     coef2 = data.readline()
# print(f'Сомножители на позициях')
# print(coef1, end=' и ')
# print(coef2, end=' дают результат: ')
#
# print(result[int(coef1)]*(result[int(coef2)]))

