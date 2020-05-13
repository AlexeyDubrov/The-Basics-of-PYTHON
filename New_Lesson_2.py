#  -------------------------------------------------------- 1 ----------------------------------------------------------


my_list = [1, -2, False, 3.4, "Help", [1, 2, 3]]
p = dict()

for n in range(len(my_list)):
    p[n] = type(my_list[n])

print(p)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, frozenset(),
           range(11), (b'twelve'), bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list):
    print(f"{i}) {item} - {type(item)}")

#  -------------------------------------------------------- 2 ----------------------------------------------------------


my_list = list(input("Enter the numbers with out space - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


a = input('Введите элементы для массива разделяя их пробелами: ').split()
i = 0
print(f'Оригинальный список {a}')
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i + 1))
    i += 1
print(f'Измененный список {a}')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


seasons_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
season = int(input("Enter the month number - "))

for i in range(len(seasons_list)):
    if season == i + 1:
        if 3 <= season <= 5:
            print(f"This is Spring, month - {seasons_list[i]}")
        elif 6 <= season <= 8:
            print(f"This is Summer, month - {seasons_list[i]}")
        elif 9 <= season <= 11:
            print(f"This is Autumn, month - {seasons_list[i]}")
        else:
            print(f"This is Winter, month - {seasons_list[i]}")

#  -------------------------------------- вариант со словарём ----------------------------------------------------------


seasons_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}
season = int(input("Enter the month number - "))

for i in range(len(seasons_dict)):
    if season == i + 1:
        if 3 <= season <= 5:
            print(f"This is Spring, month - {seasons_dict.get(i + 1)}")
        elif 6 <= season <= 8:
            print(f"This is Summer, month - {seasons_dict.get(i + 1)}")
        elif 9 <= season <= 11:
            print(f"This is Autumn, month - {seasons_dict.get(i + 1)}")
        else:
            print(f"This is Winter, month - {seasons_dict.get(i + 1)}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


# variant with dictionary
print("Variant with dictionary")
seasons = ["winter", "winter", "spring", "spring", "spring", "summer",
           "summer", "summer", "autumn", "autumn", "autumn", "winter"]
list_12 = (x for x in range(1, 13))
months = dict(zip(list_12, seasons))
user_month_number = input("Please enter a month's number:\n")
try:
    user_season = months.get(int(user_month_number))
except ValueError:
    print("you entered not a digit!")
    user_season = None
if user_season:
    print(f"It's {user_season}")
else:
    print("This month doesn't exist!")

# variant with list
print("Variant with list")
try:
    if int(user_month_number) < 1:
        print("This month doesn't exist!")
        exit(0)
    try:
        print(f"It's {seasons[int(user_month_number) - 1]}")
    except IndexError:
        print("This month doesn't exist!")
except ValueError:
    print("you entered not a digit!")

#  -------------------------------------------------------- 4 ----------------------------------------------------------


string = (input("Enter the numbers with space - ")).split()
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, (string[i])[:10])

#  ------------------------------------------- вариант решения ---------------------------------------------------------


string = (input("Enter the numbers with space - ")).split()

for n, i in enumerate(string):
    print(n + 1, i) if len(i) <= 10 else print(n, (i[:10]))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


my_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')

#  -------------------------------------------------------- 5 ----------------------------------------------------------


my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), number)
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break

#  ------------------------------------------- вариант решения ---------------------------------------------------------


rating = [7, 5, 3, 3, 2]
print(f'\nRating: {rating}')
print('Enter some natural numbers. Press Enter to exit... ')

while True:
    n = input(' > ')
    if n == '':  # если нажата клавиша Enter - выход из цикла
        break
    try:
        n = int(n)
    except ValueError:
        print('Incorrect value.')
        continue
    if n < 0:
        print('Incorrect value.')
        continue
    for i, val in enumerate(rating):
        if n > val:
            rating.insert(i, n)
            break
    else:
        rating.append(n)
    print(f'{rating}')

#  ------------------------------------------- вариант решения ---------------------------------------------------------

rating = [9, 8, 7, 7, 6, 5, 4, 3, 3, 3, 2, 1]
new = int(input('Enter some number'))

if new in rating:
    rating.reverse()
    index = rating.index(new)
    rating.insert(index, new)
    rating.reverse()
else:
    if min(rating) > new:
        rating.extend([new])
    else:
        for i in range(len(rating)):
            if rating[i] < new:
                rating.insert(i, new)
                break
print(rating)

#  -------------------------------------------------------- 6 ----------------------------------------------------------


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        features[f] = int(_) if (f == 'цена' or f == 'количество') else _  # Меняем тип числовых свойства
        analytics[f].append(features[f])  # Добавляем свойство в аналитику
    goods.append((num, features))  # Добавляем свойство в список товаров
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


i = 1
database = []
analytics = []
list_ = dict()

while True:
    start = input("Hi! I'm a database of goods. If you want to continue, enter 1. Finish - 0.\n -- ")
    if start == "0":
        l = []
        print("Do you want to do analytics?")
        answer = input("Yes - y, No - n ")
        while answer == "y":
            type_ = input("Enter analytics parameter: name, price, number, units - ")
            for j in range(len(database)):
                l.append(analytics[j].get(type_))
                list_[type_] = l
            answer = input("Do you want continue? Yes - y, No - n ")
        if answer == "n":
            if database:
                print(database)
            else:
                print("You have left the program")
        else:
            print("You mast enter 'y' or 'n'")
        print(database)
        print(list_)
        break
    elif start == "1":
        good_ = dict()
        good_["name"] = input("Enter name of good - ")
        good_["price"] = input("Enter price of good - ")
        good_["number"] = input("Enter number of good - ")
        good_["units"] = input("Enter units of good - ")
        database.append((i, good_))
        analytics.append(good_)
        i += 1
    else:
        print("You didn't enter the required numbers - 0 or 1.")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

enter = ''
goods = []
i = 0

while enter == '':  # если нажата клавиша Enter - вводим данные, иначе выходим
    i += 1

    name = input('\nEnter name of good: ')
    price = input('Enter price: ')
    num = input('Enter quantity of good: ')
    unit = input('Enter unit: ')

    goods.append((i, {'name': name, 'price': price, 'num': num, 'unit': unit}))
    print('\n', goods)

    enter = input('\nPress Enter for continue, any key+Enter to exit...')

# вывод "аналитики"
while True:
    print('\nChoose action: ')
    print(' [1] Print list of goods.')
    print(' [2] Print list of prices.')
    print(' [3] Print quantities.')
    print(' [4] Print units.')
    print(' [5] Exit.')

    action = input('\nYour choice: ')
    if action == '5':
        break

    names = ('Goods', 'Prices', 'Quantities', 'Units')
    titles = ('name', 'price', 'num', 'unit')
    res = {'name': [], 'price': [], 'num': [], 'unit': set()}

    for id, v in goods:
        res['name'].append(v['name'])
        res['price'].append(v['price'])
        res['num'].append(v['num'])
        res['unit'].add(v['unit'])

    print(res)

    print(f'\n{names[int(action) - 1]}: {res[titles[int(action) - 1]]}')

print('\nGoodbye!')
