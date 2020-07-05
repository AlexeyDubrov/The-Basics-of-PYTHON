"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""

i = int(input('Введите количество слов в списке: '))
my_list = []
while i > 0:
    str = input('Введите слово: ')
    my_list.append(str)
    i -= 1
    print (my_list, sep=' ')
    for index, value in enumerate(my_list, 1):
        if (len(value)) >  10:
            print ("{}: {}".format(index, value[:10]))
        else:
            print ("{}: {}".format(index, value))


