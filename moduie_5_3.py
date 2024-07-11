# Домашняя работа по уроку "Перегрузка операторов."
#
# Цель: применить знания о перегурзке арифметических операторов и операторов сравнения.
#
# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False
#
# Примечания:
# Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__.
# Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.

def convert_parameters(new_list = None):

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
        return f'"Название: {self.name}. кол-во этажей: {self.number_of_floor}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
