#Создать текстовый файл (не программно), сохранить в нем несколько строк,
#выполнить подсчет количества строк, количества слов в каждой строке.
with open("my_file_1.txt") as my_f:
    content = my_f.readlines()
    print(f"Количество строк в файле - {len(content)}")

with open("my_file_1.txt") as my_f:
    content = my_f.readlines()
    for i in range(len(content)):
        print(f'Количество символов {i + 1} строки {len(content[i])}')
