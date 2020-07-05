revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
staff = int(input("Введите численность персонала: "))
result = revenue - costs
if result > 0:
    print(f"Финансовый результат прибыль - {result} рублей")
    print(f"Рентабельность выручки составляет {(result/revenue)*100}%")
    print(f"Прибыль фирмы на одного сотрудника - {result/staff} рублей")
else:
    print(f"Финансовый результат - убыток {(abs(result))} рублей")