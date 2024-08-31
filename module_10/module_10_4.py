# Домашнее задание по теме "Очереди для обмена данными между потоками."
#
# Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
import queue
import random
from threading import Thread
from time import sleep
q = queue.Queue()


class Table:
    """
    Объекты этого класса должны создаваться следующим способом - Table(1)
    Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    """
    #Должен наследоваться от класса Thread (быть потоком).
    Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    Обладать атрибутом name - имя гостя.
    Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        """
        метод run, где происходит ожидание случайным образом от 3 до 10 секунд.
        :return:
        """
        timeout = random.randint(3, 10)
        sleep(timeout)


class Cafe:
    """
    Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
    Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    """
    def __init__(self, q, *tables):
        self.queue = q
        self.tables = tables

    def guest_arrival(self, *guests):
        """
        Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и
        выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение
        "<имя гостя> в очереди".
        :param guests:
        :return:
        """
        for guest in guests:
            client_on_site = False
            for table in self.tables:
                if table.guest is not None:
                    continue  # стол занят
                else:
                    table.guest = guest
                    guest.start()
                    # guest.join()
                    client_on_site = True
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    break
            if not client_on_site:
                q.put(guest)
                print(f'{guest.name} в очереди')
            self.queue = q

    def discuss_guests(self):
        """
        Этот метод имитирует процесс обслуживания гостей.
        Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
        Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
        то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и
        "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
        Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу
        присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди>
        вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>" Далее запустить поток этого гостя (start)
        :return:
        """

        while not self.queue.empty() or len(occupied_tables(self)) > 0:

            for table in occupied_tables(self):
                if not table.guest.is_alive():
                    print(f'{table.guest.name} за {table.number} столом покушал(а) и ушлел(а).')
                    print(f'Стол немер {table.number} свободен.')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                        table.guest.start()


def occupied_tables(self):
    list_tables = [table for table in self.tables if table.guest is not None]
    return list_tables


# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
# и их обслуживания (discuss_guests).
#
# Пример результата выполнения программы:
# Выполняемый код:
# class Table:
# ...
# class Guest:
# ...
# class Cafe:
# ...
# # Создание столов


tables = [Table(number) for number in range(6)]
# Имена гостей
guests_names = [
                'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# print(guests)
# Заполнение кафе столами
cafe = Cafe(*tables)
# for table in cafe.tables:
#     print(table.guest)
#     print(table.number)
# Приём гостей
cafe.guest_arrival(*guests)
# print(cafe.queue)
# Обслуживание гостей
cafe.discuss_guests()

#
# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
# Примечания:
# Для проверки значения на None используйте оператор is (table.guest is None).
# Для добавления в очередь используйте метод put, для взятия - get.
# Для проверки пустоты очереди используйте метод empty.
# Для проверки выполнения потока в текущий момент используйте метод is_alive.
# Файл module_10_4.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
