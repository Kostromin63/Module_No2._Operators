# Домашнее задание по теме "Создание потоков".
# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name)
#
from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    """
    Где word_count - количество записываемых слов,
    file_name - название файла, куда будут записываться слова.
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
    после записи каждого на 0.1 секунду.
    Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
    В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
    :param word_count:
    :param file_name:
    :return:
    """
    # date_start = datetime.now()

    with open(file_name, 'w',  encoding='utf-8') as file:
        new_text = ''
        for i in range(word_count):
            new_text = new_text + f'\nКакое-то слово № {i+1}'
            sleep(0.1)
        file.write(new_text)
    print(f'"Завершилась запись в файл {file_name}"')

    # date_end = datetime.now()
    # lead_time_func = date_end - date_start
    # print(f'Время выполнения записи в файл "{file_name}": {lead_time_func}')


# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
date_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

date_end = datetime.now()
lead_time_func = date_end - date_start
print(f'Общее время выполнения функциЙ записи в файлы 1-4: {lead_time_func}')

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
date_start = datetime.now()

thread_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

date_end = datetime.now()
lead_time_func = date_end - date_start
print(f'Общее время выполнения потоков записи в файлы 5-8: {lead_time_func}')

# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать
# рассказано в лекции к домашнему заданию.
#
# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков
# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
#
# Записанные данные в файл должны выглядеть так:
#
#
# Примечания:
# Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках
# не должно превышать ~20 секунд, а в функциях ~34 секунды.
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt,
# т.к. потоки работали почти одновременно.
# Файл module_10_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
