# Домашняя работа по уроку "Специальные методы классов"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
#
# Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20

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

    def __len__(self):
        return self.number_of_floor

    def __str__(self):  #  __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'"Название: {self.name}. кол-во этажей: {self.number_of_floor}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
