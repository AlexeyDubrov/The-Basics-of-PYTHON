#  -------------------------------------------------------- 1 ----------------------------------------------------------


while True:
    line = input("Enter - ").split()
    if not line:
        break
    with open("text.txt", "a") as my_file:
        for i in range(len(line)):
            print(line[i], file=my_file)
            #  my_file.write(line[i] + '\n')

#  -------------------------------------------------------- 2 ----------------------------------------------------------


counter = 0
with open("text_2.txt", "r") as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split(' ')
        print(line, 'Длина строки: ', len(line_words))
    print('Всего строк: ', counter)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


with open("text_2.txt") as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line):
        number_of_words = len(value.split())
        print('Строка {} содержит {} слов'.format(index + 1, number_of_words))

#  -------------------------------------------------------- 3 ----------------------------------------------------------


with open("text_3.txt", "r") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f"Salary less 20 000 {less}. Average salary - {sum(map(int, s_sum)) / len(s_sum)}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def task_3():
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')


task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')

#  -------------------------------------------------------- 4 ----------------------------------------------------------


rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "a") as new_file:
    with open("text_4.txt") as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dic[i[0]] + ' - ' + i[1] + "\n")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from random import randint

sum_el = 0
with open("text.txt", "w") as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + " ")

print(f"Sum of elements - {sum_el}")

#  -------------------------------------------------------- 6 ----------------------------------------------------------


with open('text_6.txt') as my_file:mydict = {}
with open("text_6.txt", "r") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        namesum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mydict[name] = namesum
print(f"{mydict}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------

plan = {}
hours = []
with open("text_6.txt") as lesson5_6:
    for subject in lesson5_6:
        subject_split = subject.split()
        subject_name = subject_split[0]
        all_hours = subject_split[1:]
        plan[subject_name] = 0
        for types in all_hours:
            try:
                plan[subject_name] += int(types[:types.find("(")])
            except ValueError:
                pass
print(plan)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from re import findall

d = dict()

with open('text_6.txt', 'r') as f:
    for line in f:
        key = findall('\w*', line)[0]
        values = [int(i) for i in findall('\d+', line)]
        s = 0
        for v in values:
            s += v
        d[key] = s
print(d)

#  -------------------------------------------------------- 7 ----------------------------------------------------------

import json

with open('07listFirm.txt', 'r', encoding='utf-8') as fIn:
    allProfit = []
    allFirms = []
    dallFirmProfit = {}
    for sLine in fIn:
        sline = sLine[:-1]
        lLine = sLine.split()
        try:
            lLine[2] = int(lLine[2])
            lLine[3] = int(lLine[3])
        except ValueError:
            print('Некоректные данные в исходном файле')
            exit()
        profit = lLine[2] - lLine[3]
        lLine.append(profit)
        dallFirmProfit[f'{lLine[1]} \'{lLine[0]}\''] = profit
        if profit > 0:
            # Прибыль
            allProfit.append(profit)

averageProfit = sum(allProfit) / len(allProfit)
dAverageProfit = {}
dAverageProfit['average_profit'] = averageProfit
result = [dallFirmProfit, dAverageProfit]

with open("my_file.json", 'w', encoding='utf-8') as fOut:
    json.dump(result, fOut)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import json
import codecs

with codecs.open("text_77.json", "w", encoding='utf-8') as j_file:
    with open('text_7.txt', encoding='utf-8') as my_file:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = my_file.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["average_profit"] = k/o
        all_list = [subjects, middle]
        json.dump(all_list, j_file, ensure_ascii=False, indent=4)


print(f"All information on firms:\n{line}\n\nTotal list:\n{all_list}")
