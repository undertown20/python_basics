# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))
summ = 0

for i in range(0, n):
    summ += int(str(n) + i * str(n))
print(summ)