# Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
#
# Задача:

def all_variants(text, number_iteration=1):
    """
    принимает строку text и возвращает объект-генератор,
    при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
    :param number_iteration:
    :param text:
    :return:
    """
    # if number_iteration == " ":  # Начало рекурсии
    #     number_iteration = 1
    # else:
    number_iteration = int(number_iteration)
    number_of_iterations = len(text)
    # end = len(text)

    for i in range(number_of_iterations):
        first_index = i
        second_index = first_index + number_iteration
        if len(text[first_index: second_index]) == number_iteration:
            yield text[first_index: second_index]
    number_iteration = number_iteration + 1
    if number_iteration <= number_of_iterations:
        yield from all_variants(text, number_iteration)
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:


a = all_variants("abc")
for i in a:
    print(i)

b = all_variants("abcde")
for i in b:
    print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
#
# Примечания:
# Для функции генератора используйте оператор yield.
#
# Файл module_9_6.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
