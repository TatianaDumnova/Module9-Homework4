# Домашнее задание по теме "Генераторы"
# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки. В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield
# Входные данные
# a = all_variants("abc")
# for i in a:
# print(i)
# Выходные данные
# a
# b
# c
# ab
# bc
# abc
#
# Часто задаваемые вопросы:
# один из вариантов функции генерирующей все последовательные подстроки
# def all_variants(text):
# for start in range(len(text)):
# for end in range(start+1, len(text)+1):
# yield text[start:end]
#
# for substr in all_variants('12345'):
# print(substr)

def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


for i in all_variants("abc"):
    print(i)
