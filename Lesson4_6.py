# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,

from itertools import count
from itertools import cycle

for el in count(20):
    if el > 50:
        break
    else:
        print(el)

# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

cats = ["grey", "red", "black", "white"]
iter = cycle(cats)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))