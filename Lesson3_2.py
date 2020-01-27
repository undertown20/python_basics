# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def dataInquiry(**kwargs):
    return list(kwargs.values())


def dataInquiry_use():
    print(dataInquiry(name=input('Enter name: '),
                s_name=input('Enter second name: '),
                b_date=input('Enter birth day: '),
                l_town=input('Enter live town: '),
                email=input('Enter email: '),
                tel=input('Enter tel number: ')))
print(dataInquiry_use())
