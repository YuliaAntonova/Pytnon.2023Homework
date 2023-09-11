"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N"""
number = int(input('Введите число: '))
composition = 1
i = 0
while composition < number:
    composition = 2**i
    print(composition)
    i += 1

# for i in number:
#     composition = 2**i
#     print(composition)
