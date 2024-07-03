# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объек
# та self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
#
# Пример результата выполнения программы:
# Исходные данные:
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
# Примечания:
# self - это переменная указывающая на объект. Используйте её для обращения к атрибутам или методам объекта.
# Обращение к атрибутам или методам объекта/класса происходит при помощи "."
# Метод __init__ вызывается в момент создания объекта.

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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
