#  4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
string = input("Введите строку (несколько слов или предложение). ")
words = []
numbers = 1
for i in range(string.count(' ') + 1):
    words = string.split()
    if len(str(words)) <= 10:
        print(f" {numbers} {words [i]}")
        numbers += 1
    else:
        print(f" {numbers} {words [i] [0:10]}")
        numbers += 1