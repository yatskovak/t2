"""
6. (МОДУЛЬ 2) В проекте создать новый модуль bornyear.py
7. Написать программу используя условные операторы:
- Спросить у пользователя год рождения А.С Пушкина
- Если пользователь ввел верный год вывести 'Верно'
- Если пользователь ошибся вывести 'Неверно'
"""


b_year_asp = input("Введите год рождения А.С Пушкина - ")

if b_year_asp == "1799": #  1799 - в кавычках т.к. Input-вводит строки type - str
    print('Верно')
    print(b_year_asp, "  ====  ", type(b_year_asp))
else:
    print('Неверно')
    print(b_year_asp, "  ====  ", type(b_year_asp))




"""
#  1799 можно без кавычек, тогда надо переменную полученную в INPUT
#  преобразовать в целое

aaa  = input("Введите год рождения А.С Пушкина  -")
b_year_asp = int(aaa)

if b_year_asp == 1799:
    print('Верно')
    print(b_year_asp, "  ====  ", type(b_year_asp))
else:
    print('Неверно')
    print(b_year_asp, "  ====  ", type(b_year_asp))
"""