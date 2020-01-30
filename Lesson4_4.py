#4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

import random

N = 10

L, Exists = list(), list()

for i in range(N):
    L.append(random.randint(0, 10))
    Exists.append(True)

print(f"Изначальный список: {L}")

for i in range(N):
    if Exists[i]:
        for j in range(i + 1, N):
            if L[j] == L[i]:
                Exists[j] = False

print("Итоговый список:")
for i in range(N):
    if Exists[i]:
        print(str(L[i]) + " ")