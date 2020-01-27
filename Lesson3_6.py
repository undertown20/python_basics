# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    word = []
    for i in range(len(text)):
        word.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(word)

print(int_func(input("Введите текст: ").split()))

def int_func_2(text):
    words = []
    for i in range(len(text)):
        words.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(words)

print(int_func_2(input("Введите слова через пробел: ").split()))