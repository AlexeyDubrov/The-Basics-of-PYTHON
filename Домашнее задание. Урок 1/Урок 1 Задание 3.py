#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input('Введите число: '))
n1 =int('%d' % n)
n2=int('%d%d' % (n,n))
n3=int('%d%d%d' % (n,n,n))
print(n1 + n2 + n3)


