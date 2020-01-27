# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(numb1, numb2):
    try:
        return numb1 / numb2
    except ZeroDivisionError:
        return "Нельзя делить на 0"
    except ValueError:
        return 'No value'

print(division((int(input("Введите первое число: "))), (int(input("Введите второе число: ")))))