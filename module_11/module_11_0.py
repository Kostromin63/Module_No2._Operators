# Домашнее задание по теме "Интроспекция"
# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
#
# Файл с кодом прикрепите к домашнему заданию.

import inspect
from threading import Thread


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.paid = False

    def control(self):
        pass

    def _control(self):
        pass

    def run(self):
        pass


def func():
    pass


def introspection_info(obj):
    """
    принимает объект obj
    :param obj:
    :return
    Верните словарь или строки с данными об объекте, включающий следующую информацию:
    - Тип объекта.
    - Атрибуты объекта.
    - Методы объекта.
    - Модуль, к которому объект принадлежит.
    - Другие интересные свойства объекта, учитывая его тип (по желанию):
    """

    info = {}
    attributes = []
    methods = []

    info['type'] = type(obj)

    for attribute in dir(obj):
        a = type(getattr(obj, attribute))
        if str(a).find('method') >= 0:
            methods.append(attribute)
        elif str(a) == "<class 'str'>":
            attributes.append(attribute)

    info['attributes'] = attributes
    info['methods'] = methods
    info['module'] = inspect.getmodule(obj)

    if isinstance(obj, str):
        info['length_str'] = len(obj)
    elif isinstance(obj, int):
        number_str = str(obj)
        list_number = []
        for number in number_str:
            list_number.append(int(number))
        info['sum_all_nuvber'] = sum(list_number)

    return info


# Пример работы с числом
number_info = introspection_info(42)
print(number_info)

# Пример работы со строками
string_info = introspection_info('Vasiliy')
print(string_info)

# Пример работы с классом
g1 = Guest('Vasya')
class_info = introspection_info(g1)
print(class_info)

# Пример работы с функцией
func_info = introspection_info(func)
print(func_info)
