"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv
work_hours, rate_hours, bonus = argv
res = work_hours * rate_hours + bonus
print(f"Заработная плата равна {res} у.е.")

#ValueError: not enough values to unpack (expected 3, got 1) Где я ему не додал значений, так и не понял )