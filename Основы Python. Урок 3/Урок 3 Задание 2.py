"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def information(**kwargs):
    return kwargs

print(information(name = "Alex", surname = "Dubrov", year = 1976, city = "Klin", email = "email", telefone_number = 223322))
