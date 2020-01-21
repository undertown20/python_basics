#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

list = [8, 7, 5, 2, 6]
print(list)
r = int(input("Введите новый элемент рейтинга "))
for i in range(len(list)):
    if list[i] == r:
        list.insert(i + 1, r)
        break
    elif list[0] < r:
        list.insert(0, r)
        break
    elif list[-1] > r:
        list.append(r)
        break
    elif list[i] > r and list[i + 1] < r:
        list.insert(i + 1, r)
        break

print(list)