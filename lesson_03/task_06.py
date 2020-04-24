# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(word):
    chars = list(word)
    chars[0] = chr(ord(chars[0]) - 32)
    return ''.join(chars)


print(int_func('text'))

string = 'hello world. python is the best!'
words = string.split()

capitalized_words = []
for w in words:
    capitalized_words.append(int_func(w))

capitalized_string = ' '.join(capitalized_words)
print(capitalized_string)
