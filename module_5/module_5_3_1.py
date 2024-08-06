# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
#
# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.
#
# Дополнительно о работе метода __new__:
# Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
# Разберёмся, как происходит передача данных между ними на следующем примере:
# class Example:
#   def __new__(cls, *args, **kwargs):
#   print(args)
#     print(kwargs)
#     return object.__new__(cls)
#
#   def __init__(self, first, second, third):
#   print(first)
#   print(second)
#     print(third)
#
# ex = Example('data', second=25, third=3.14)
#
# Работа __new__:
# 'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0
# как единственный элемент кортежа.
# second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться
# под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
# Передача данных из __new__ в __init__:
# После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
# В параметр first распакуется из args единственный аргумент 'data'.
# В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
# В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
#
#
# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам
# класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута
# houses_history.
#
# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# # Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
#
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории

def convert_parameters(new_list=None):

    if isinstance(new_list[0], int):
        pass
    elif isinstance(new_list[0], House):
        int_self = new_list[0].number_of_floor
        new_list.pop(0)
        new_list.insert(0, int_self)
    if isinstance(new_list[1], int):
        pass
    elif isinstance(new_list[1], House):
        int_other = new_list[1].number_of_floor
        new_list.pop(1)
        new_list.insert(1, int_other)
    return new_list


class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):

        if new_floor > self.number_of_floor:
            print('Такого этажа не существует.')

        elif new_floor == 1:
            print('Вы уже находитесь на 1 этаже.')
        elif new_floor < 1:
            print('На подземную парковку спуститесь по лестнице.')
        else:
            current_floor = 1
            print('Поехали.')
            while current_floor < new_floor:
                print('Этаж: ' + str(current_floor))
                current_floor += 1
            print('Приехали, это ' + str(current_floor) + ' этаж.')

    def __eq__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] == new_list[1]

    def __lt__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] < new_list[1]

    def __le__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] <= new_list[1]

    def __gt__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] > new_list[1]

    def __ge__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] >= new_list[1]

    def __ne__(self, other):
        int_self = self
        int_other = other
        new_list = convert_parameters([int_self, int_other])
        return new_list[0] != new_list[1]

    def __add__(self, value):
        int_self = self
        int_other = value
        new_list = convert_parameters([int_self, int_other])
        self.number_of_floor = new_list[0] + new_list[1]
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'"Название: {self.name}. кол-во этажей: {self.number_of_floor}"'

    def __del__(self):
        print(f'"{self.name} снесён, но он останется в истории"')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
