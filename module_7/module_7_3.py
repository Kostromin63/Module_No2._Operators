# Домашнее задание по теме "Оператор "with".
#
# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
#
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
#
# Также объект класса WordsFinder должен обладать следующими методами:
#
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря
# - item().
#
# for name, words in get_all_words().items():
#   # Логика методов find или count
#
# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:
# It`s a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text
#


class WordsFinder:
    """
    WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
    Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в
    атрибут file_names в виде списка или кортежа. В методах find и count пользуйтесь ранее написанным методом
    get_all_words для получения названия файла и списка его слов.
    """
    def __init__(self, *args):
        self.file_name = args

    def get_all_words(self):
        """
        get_all_words - подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        Где:
        'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        Алгоритм получения словаря такого вида в методе get_all_words:
        Создайте пустой словарь all_words.
        Переберите названия файлов и открывайте каждый из них, используя оператор with.
        Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
        Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не
        дефис в слове).
        Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
        В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
        """
        all_words = {}
        geyrnawbb_symbol = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_name:
            with open(i, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                _str = ''.join(lines)
                _str = _str.lower()
                _str = _str.split()
                for symbol in _str:
                    if symbol in geyrnawbb_symbol:
                        _str = _str.replace(symbol, '')
                all_words[i] = _str
                return all_words

    def find(self, word):
        """
        find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
        позиция первого такого слова в списке слов этого файла.
        """
        word = word.lower()
        _dict = self.get_all_words()
        for i in _dict:
            text_from_file = _dict[i]
            counter = 0
            for word_from_file in text_from_file:
                counter = counter + 1
                if word_from_file == word:
                    result = {i: counter}
                    return result

    def count(self, word):
        """
        count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
        количество слова word в списке слов этого файла.
        """
        word = word.lower()
        _dict = self.get_all_words()
        result = {}
        counter = 0
        for i in _dict:
            text_from_file = _dict[i]
            for word_from_file in text_from_file:
                if word_from_file == word:
                    counter = counter + 1
                result = {i: counter}
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
#
# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
# 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
