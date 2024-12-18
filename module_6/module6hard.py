# Дополнительное практическое задание по модулю: "Наследование классов."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и
# трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного
# использования таких объектов?
#
# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон,
# цвет и др.
#
# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование
# (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
#
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами
# изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия
# (методы) - геттеры и сеттеры.
#
# Файл с кодом (module6hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий
# с файлом решения.

import math


class Figure:
    """
    Атрибуты класса Figure: sides_count = 0
    Каждый объект класса Figure должен обладать следующими атрибутами:
    Атрибуты(инкапсулированные):
    __sides(список сторон (целые числа)),
    __color(список цветов в формате RGB)
    Атрибуты(публичные):
    filled(закрашенный, bool)
    """

    sides_count = 0

    def __init__(self, __color, *args):

        if not self.set_sides(*args):  # нет записи сторон
            side = 1
            if len(args) == 1:
                side = args[0]
            self.__sides = [side] * self.sides_count
        if self.__is_valid_color(__color):
            self.__color = __color
        self.filled = False

    def get_color(self):
        """
        Метод get_color, возвращает список RGB цветов.
        :return: __color
        """
        return self.__color

    @staticmethod
    def __is_valid_color(color):
        """
        Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
        значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
        от 0 до 255 (включительно).
        :param color:
        :return: bool
        """
        for i in color:
            if not 0 <= i <= 255 and isinstance(i, int):
                return False
        return True

    def set_color(self, r, g, b):
        """
        Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        :param r:
        :param g:
        :param b:
        :return:
        """
        color = [r, g, b]
        if self.__is_valid_color(color):
            self.__color = color
        else:
            print(f'Неверные параметры цвета. Цвет не изменен.')

    def get_sides(self):
        """
        Метод get_sides должен возвращать значение я атрибута __sides.
        :return: __sides
        """
        return self.__sides

    def __len__(self):
        """
        Метод __len__ должен возвращать периметр фигуры.
        :return: sum __sides
        """
        return sum(self.__sides)

    def __is_valid_sides(self, new_sides):
        """
        Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
        целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        :param new_sides:
        :return: bool
        """
        if self.sides_count != len(new_sides):
            return False

        for i in new_sides:
            if not isinstance(i, int) and i <= 0:
                return False

        if isinstance(self, Triangle):
            a = new_sides[0]
            b = new_sides[1]
            c = new_sides[2]
            if ((a+b) < c) or ((b+c) < a) or ((a + c) < b):
                return False
        elif isinstance(self, Cube):
            side = new_sides[0]
            if not all(side == i for i in new_sides):
                return False
        return True

    def set_sides(self, *new_sides):
        """
        Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
        то не изменять, в противном случае - менять.
        :param self:
        :param new_sides:
        :return: bool
        """
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
            return True
        else:
            # print(f'Передано не верное количество сторон для фигуры.')
            return False


class Circle(Figure):
    """
    Атрибуты класса Circle: sides_count = 1
    Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    """
    sides_count = 1

    def __init__(self, __color, *args):
        super().__init__(__color, *args)
        self.__radius = self.set_radius()

    def get_square(self):
        """
        Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        :return:
        """
        return sum(super().get_sides()) ** 2 / (4 * math.pi)

    def get_radius(self):
        return self.__radius

    def set_radius(self):
        return sum(super().get_sides()) / (2 * math.pi)


class Triangle(Figure):
    """
    Атрибуты класса Triangle: sides_count = 3
    Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    Метод get_square возвращает площадь треугольника.
    """
    sides_count = 3

    def __init__(self, __color, *args):
        super().__init__(__color, *args)
        self.__height = 0

    def get_square(self):
        p = self.__len__() / 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        #  s1 = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(s, 3)


class Cube(Figure):
    """
    Атрибуты класса Cube: sides_count = 12
    Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure.
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    Метод get_volume, возвращает объём куба.
    """

    sides_count = 12

    def __init__(self, __color, *args):
        super().__init__(__color, *args)

    def get_volume(self):
        return super().get_sides()[0] ** 3


# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
# то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
