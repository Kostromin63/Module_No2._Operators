# Домашнее задание по теме "Логирование"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное
# значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
import logging

# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#


from rt_with_exceptions import Runner
import unittest

logging.basicConfig(filemode='w', filename='runner_tests.log', encoding='utf-8', level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    """
    Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest
    """
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk
         у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
        :return:
        Дополните методы тестирования в классе RunnerTest следующим образом:
        test_walk:
        Оберните основной код конструкцией try-except.
        При создании объекта Runner передавайте отрицательное значение в speed.
        В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
        В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
        "Неверная скорость для Runner".
        """
        try:
            vasya = Runner('Vasya', -5)
            for i in range(10):
                vasya.walk()
            self.assertEqual(vasya.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'"Неверная скорость для Runner".', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
         этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
        :return:
        Дополните методы тестирования в классе RunnerTest следующим образом:
        test_run:
        Оберните основной код конструкцией try-except.
        При создании объекта Runner передавайте что-то кроме строки в name.
        В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
        В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
         "Неверный
        тип данных для объекта Runner".
        """
        try:
            petya = Runner(5)
            for i in range(10):
                petya.run()
            self.assertEqual(petya.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('"Неверный тип данных для объекта Runner".', exc_info=True)

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

# Пример результата выполнения программы:
# Пример полученного файла логов runner_tests.log:
#
# Файл tests_12_4.py с классами тестов и runner_tests.log с логами тестов загрузите на ваш GitHub репозиторий.
# В решении пришлите ссылку на него.
# Успехов!
