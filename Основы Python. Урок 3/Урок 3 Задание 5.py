"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу."""

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