# Домашнее задание по теме "Простые Юнит-Тесты"
#
# Цель: приобрести навык создания простейших Юнит-тестов
#
# Задача "Проверка на выносливость":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
#
# . В классе пропишите следующие методы:
# test_walk
# test_run
# test_challenge
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
#
# Пункты задачи:
# Скачайте исходный код для тестов.
# Создайте класс RunnerTest и соответствующие описанию методы.
# Запустите RunnerTest и убедитесь в правильности результатов.
# Пример результата выполнения программы:
# Вывод на консоль:
# Ran 3 tests in 0.001s OK
#
# Примечания:
# Попробуйте поменять значения в одном из тестов, результаты

from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    """
    Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest
    """
    is_frozen = False
    # @classmethod
    # def setUpClass(self):
    #     """
    #     Класс RunnerTest дополнить атрибутом is_frozen = False
    #     """
    #     self.is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk
         у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
        :return:
        """
        vasya = Runner('Vasya')
        for i in range(10):
            vasya.walk()
        self.assertEqual(vasya.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
         этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
        :return:
        """
        petya = Runner('Petya')
        for i in range(10):
            petya.run()
        self.assertEqual(petya.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        """
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у
        объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте
        метод assertNotEqual, чтобы убедится в неравенстве результатов.
        :return:
        """
        olya = Runner('Olya')
        masha = Runner('Masha')
        for i in range(10):
            olya.run()
            masha.walk()
        self.assertNotEqual(masha.distance, olya.distance)


if __name__ == "__main__":
    unittest.main()
