num = int(input("Введите число: "))
max_num = 0
while num > 0:
    last_num = num%10 #никогда бы не догадался о таком способе
    num = num//10
    if last_num > max_num:
        max_num = last_num
print("Самая большая цифра в числе: ", max_num)

