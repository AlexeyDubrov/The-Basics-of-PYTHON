# Создать программно файл в текстовом формате, записать в него построчно данные,
#   вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

f = open("my_file.txt", 'w')
line = input("Введите текст: \n")
while True:
    f.writelines(line)
    line = input("Введите текст: \n")
    if not line:
        break

f.close()
with open("my_file.txt") as f:
    content = f.read()
print(content)


