#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)
#РЕШЕНИЕ ДЗ СТАРОЕ
# def factorial_list(n):
#     return [list(range(1, n + 1))
#     for n in range(1, n + 1)]
# print(f'Список факториалов по возрастанию от 1 до 4: {factorial_list(4)}')

# #РЕШЕНИЕ ДЗ ПО-НОВОМУ C ТЕРНАРНЫМ ОПЕРАТОРОМ И LIST COMPREHENSION.
set=[];
set=[set[-1] for x in range(1,5) if not set.append(x*set[-1] if set else 1)]
print(f'Список факториалов по возрастанию от 1 до 4: {set}')