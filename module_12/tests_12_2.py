# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
#
# Задача:
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
# Появился атрибут speed для определения скорости бегуна.
# Метод __eq__ для сравнивания имён бегунов.
# Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список
# участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
import unittest
# from unittest import TestCase
import runner_and_tournament as rn


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        """
        setUpClass -метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты
        всех тестов.
        """
        self.all_results = {}

    def setUp(self):
        """
        setUp - метод, где создаются 3 объекта:
        Бегун по имени Усэйн, со скоростью 10.
        Бегун по имени Андрей, со скоростью 9.
        Бегун по имени Ник, со скоростью 3.
        :return:
        """
        usayn = rn.Runner('Усайн', 10)
        andre = rn.Runner('Андрей', 9)
        nik = rn.Runner('Ник', 3)
        self.participants = [usayn, andre, nik]

    @classmethod
    def tearDownClass(self):
        """
        tearDownClass - метод, где выводятся all_results по очереди в столбец.
        :return:
        """

        for i in self.all_results:
            dict_ = self.all_results[i]
            for j in dict_:
                item_ = dict_[j]
                if isinstance(item_, list):
                    athletes_who_took_one_place = [participant.__str__() for participant in item_]
                    dict_[j] = ', '.join(athletes_who_took_one_place)
                else:
                    dict_[j] = item_.__str__()
            print(dict_)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tournament_1(self):
        """
        Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса
        Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается
        метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и
        предполагаемое имя последнего бегуна.
        Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
        Усэйн и Ник
        Андрей и Ник
        Усэйн, Андрей и Ник.
        Как можно понять: Ник всегда должен быть последним.
        :return:
        """
        tur_1 = rn.Tournament(90, *self.participants[::2])
        result = tur_1.start()
        max_key = get_max_key(self.all_results)
        self.all_results[max_key+1] = result
        self.assertTrue(self.participants[2].__eq__(self.all_results[max_key+1][2]))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tournament_2(self):
        """
        Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса
        Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается
        метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и
        предполагаемое имя последнего бегуна.
        Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
        Усэйн и Ник
        Андрей и Ник
        Усэйн, Андрей и Ник.
        Как можно понять: Ник всегда должен быть последним.
        :return:
        """
        tur_2 = rn.Tournament(90, *self.participants[1:3])
        result = tur_2.start()
        max_key = get_max_key(self.all_results)
        self.all_results[max_key+1] = result
        self.assertTrue(self.participants[2].__eq__(self.all_results[max_key+1][2]))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tournament_3(self):
        """
        Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса
        Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается
        метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и
        предполагаемое имя последнего бегуна.
        Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
        Усэйн и Ник
        Андрей и Ник
        Усэйн, Андрей и Ник.
        Как можно понять: Ник всегда должен быть последним.
        :return:
        """
        tur_3 = rn.Tournament(90, *self.participants)
        result = tur_3.start()
        max_key = get_max_key(self.all_results)
        self.all_results[max_key+1] = result
        self.assertTrue(self.participants[2].__eq__(self.all_results[max_key+1][3]))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_true_start(self):
        """
        Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса
        Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается
        метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и
        предполагаемое имя последнего бегуна.
        Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
        Усэйн и Ник
        Андрей и Ник
        Усэйн, Андрей и Ник.
        Как можно понять: Ник всегда должен быть последним.
        :return:
        """
        # Что бы не убивать данные подготовленные в "setUp()", сформируем параметр для новой функции прямо здесь:

        usayn = rn.Runner('Усайн', 10)
        andre = rn.Runner('Андрей', 9)
        nic = rn.Runner('Николай', 10)
        vasy = rn.Runner('Вася', 3)
        grisha = rn.Runner('Гриша', 3)
        piter = rn.Runner('Петя', 6)
        vova = rn.Runner('Вова', 6)
        pasha = rn.Runner('Паша', 3)
        participants = [usayn, andre, nic, vasy, grisha, piter, vova, pasha]

        tur_true = rn.Tournament(90, *participants)
        result = tur_true.true_start()
        max_key = get_max_key(self.all_results)
        self.all_results[max_key+1] = result
        max_key_last_tournament = get_max_key(self.all_results[max_key+1])
        self.assertTrue(participants[len(participants) - 1].__eq__(self.all_results[max_key+1]
                                                                   [max_key_last_tournament][2]))


def get_max_key(dict_):
    keys = list(dict_.keys())
    if len(keys):
        keys.sort(reverse=True)
        max_key = keys[0]
    else:
        max_key = 0
    return max_key


if __name__ == '__main__':
    unittest.main()

#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы
# бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
# Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов
# и наличие всех перечисленных переопределённых методов из класса TestCase.
# Файл tests_12_2.py c классами тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
