"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N"""
number = int(input('Введите число: '))
composition = 1
# i = 0
# while composition < number:
#     print(composition)
#     composition = 2**i
#     i += 1
    # или
# for i in number:
#     composition = 2**i
#     print(composition)
while composition < number:
    print(composition, end=" ")
    composition *= 2
