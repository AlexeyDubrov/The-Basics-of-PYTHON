"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""
list_random = [1, 64, 'Python', 'декабрь', [9, 8, 7, 6], ('задание1', 'задание2', 'задание3'), {'a', 'u', 't', '4', 'gh'}, ('1:one', '2:two')]
for i in list_random:
    print(type(i))

# Второй вариант
list_random = [1, 64, 'Python', 'декабрь', [9, 8, 7, 6], ('задание1', 'задание2', 'задание3'),{'a', 'u', 't', '4', 'gh'}, ('1:one', '2:two')]
for i in list_random:
    i = int(input('Введите индекс элемента для проверки типа: '))
    print (type(list_random[i]))