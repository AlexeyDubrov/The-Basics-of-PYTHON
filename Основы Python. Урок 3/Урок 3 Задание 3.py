#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_sum(x, y, z):
    if x >= y <= z:
        sum = x + z
    elif y >= x <= z:
        sum = y + z
    elif x >= z <= y:
        sum = x + z
    return sum
result = my_sum(5, 2, 6)
print(result)