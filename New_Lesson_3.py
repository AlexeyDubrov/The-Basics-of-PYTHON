#  -------------------------------------------------------- 1 ----------------------------------------------------------


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return div_num


print(div(input("Enter first number - "), input("Enter second - ")))

#  -------------------------------------------------------- 2 ----------------------------------------------------------


def personal_info(**kwargs):
    return kwargs


print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
      birthday=input("Enter your birthday: "), city=input("Enter your city: "), email=input("Enter your email: "),
      phone_number=input("Enter your phone number: ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def person_inf(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city};" \
           f" email - {email}; phone - {phone}"


print(person_inf(name="Alice", surname="Selezneva", birthday="21.09.67", city="Moscow",
                 email="alice.selezneva@mail.ru", phone="143-91-19 "))

#  -------------------------------------------------------- 3 ----------------------------------------------------------


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "Enter only a numbers!"


print(my_func(2, 11, -30))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_func(1978, 1, 2))

#  -------------------------------------------------------- 4 ----------------------------------------------------------

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res


print(my_pow_fun(4.5, -2))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def power(x, y):
    try:
        x, y = float(x), int(y)
        res = x
        for _ in range(abs(y)-1):
            res *= x
        return f"{1/res:.4f}"
    except ValueError:
        return "Value Error"


print(power(input("Первое значение - "), input("Второе значение - ")))

#  -------------------------------------------------------- 5 ----------------------------------------------------------


def summary():
    ex = False
    fResult = 0
    while ex == False:
        lNumbers = input('Input numbers divided by whitespaces or q to quit: ').split()
        result = 0
        for i in range(len(lNumbers)):
            if lNumbers[i] == 'q':
                ex = True
                break
            else:
                result = result + int(lNumbers[i])
        fResult = fResult + result
        print(f"Current sum is {fResult}")
    print(f"You've quited! Final sum is {fResult}")

summary()

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def my_func():
    # function takes numbers lines (split by space) and sum all elements
    # verify that the numbers are entered correctly
    while True:
        try:
            inp = input("Enter your numbers with a space('q' in any position to exit after sum):\n")
            num_line = inp.split()
            # check the "q" button for exit the program
            if "q" in num_line:
                try:
                    global summ
                    num_line = list(map(float, num_line[:num_line.index("q")]))
                    summ += sum(num_line)
                    print(f"Total sum = {summ}   End of program")
                    break
                except ValueError:
                    print("Enter the numbers!\n")
            num_line = list(map(float, num_line))
            summ += sum(num_line)
            print(f"Total sum = {summ}\n")
        except ValueError:
            print("Enter the numbers!\n")


summ = 0
my_func()


#  ------------------------------------------- вариант решения ---------------------------------------------------------


def sum_fun():
    all_sum = 0
    while True:
        sum_ = 0
        args = input("Enter numbers with a space - ").split()
        try:
            for n, i in enumerate(args):
                if i != "?":
                    sum_ += int(args[n])
                else:
                    all_sum += sum_
                    return f"The all sum - {all_sum}"
            print(sum_)
            all_sum += sum_
            answer = input("Enter more numbers? y/n - ")
            if answer == "y":
                continue
            else:
                break
        except ValueError:
            return f"Enter only numbers, the all sum - {all_sum}"
    return f"The all sum - {all_sum}"


print(sum_fun())

#  ------------------------------------------- вариант решения ---------------------------------------------------------


num = 0
try:
    while num != '#':
        for i in map(int, input("Для выхода наберите '#'\nВведите числа, используя пробел.\n").split()):
            num += i
        print(num)
except ValueError:
    print(num)

#  -------------------------------------------------------- 6 ----------------------------------------------------------


def int_func(words):
    # function takes words(split by space) and uppercase first letter in any words
    # verify that the all letters its lower latin script and spaces
    for i in words:
        if not ord(i) == 32 and not 97 <= ord(i) <= 122:
            print("Lower latin script and spaces between!\n")
            words = input("Enter words with a space(lower latin script):\n")
            break
    words_list = words.split()
    for i in range(len(words_list)):
        print(words_list[i][0].upper() + words_list[i][1:], end=" ")


int_func(input("Enter words with a space(lower latin script):\n"))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


def int_func(word):
    words, result = [], []
    if len(word) > 0:
        for i in word.split():
            words.append(i[0].upper() + i[1:])
        result = ' '.join(words)
    return result

print(int_func(input("Введите строку: ")))

#  ------------------------------------------- вариант решения ---------------------------------------------------------


int_func = lambda sentence: print(sentence.title())

int_func(input("Please enter set of words. "))
