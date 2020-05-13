#  -------------------------------------------------------- 1 ----------------------------------------------------------


from sys import argv


def salary():
    try:
        time, stavka, premia = map(int, argv[1:])
        print(f"Salary - {time * stavka + premia}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = [2, 4, 1, 6, 9, 33, 7]
more_then = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(more_then)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#  -------------------------------------------------------- 3 ----------------------------------------------------------


uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

#  -------------------------------------------------------- 4 ----------------------------------------------------------

from random import randint

my_list = [randint(-10, 10) for i in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [2, 4, 6, 6, 7, 7, 8, 8, 2, 3, 1]
new_list = [el for el in dict.fromkeys(my_list)]
print(f"Исходный список: {my_list} ")
print(f"Новый список: {new_list} ")

#  -------------------------------------------------------- 5 ----------------------------------------------------------


from functools import reduce


def sum_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(sum_list, uniq_list)}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

from functools import reduce

list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(lambda a, b: a * b, list))

#  -------------------------------------------------------- 6 ----------------------------------------------------------


from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числа необходимо нажать Enter,'
      ' для выхода из программы - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print(
    'Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода'
    ' из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(start_el), 1, stop_el + 1)]
        #  repeat_list = [next(cycle(my_list)) for el in range(num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"


print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


import itertools as it

# integers iterator with checking for integer
try:
    integers = iter(i for i in it.count(int(input("Enter starting integer: "))))
    print(f"first numbers in the 'integers' iterator: {next(integers)} {next(integers)} {next(integers)}\n")
except:
    print("Error, only integers!")
# cycle iterator
my_list = ['go', 1, 2, "hello"]
print(f"List - {my_list}")
cycle_iter = iter(i for i in it.cycle(my_list))
print(f"first elements in the 'cycle' iterator: {next(cycle_iter)} {next(cycle_iter)} "
      f"{next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)}\n")

#  -------------------------------------------------------- 7 ----------------------------------------------------------

from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


generator = fibo_gen()
x = 0
for i in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")


#  ------------------------------------------- вариант решения ---------------------------------------------------------


def fibo_gen(n):
    m = 1
    for i in range(1, n):
        if i > 15:
            break
        m *= i
        yield m


for i in fibo_gen(26):
    print(i)
