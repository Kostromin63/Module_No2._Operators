# Домашняя работа по уроку "Пространство имен и способы вызова функции"
# Цель: закрепить знание использования параметров в функции и знания из предыдущих модулей.
#
# Задача("Однокоренные"):
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее
# неограниченную последовательность в параметр *other_words. Функция должна составить новый список same_words
# только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из
# этих слов. После вернуть список same_words в качестве результата своей работы.
#
# Пункты задачи:
# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *args):
    # Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    other_words = args
    same_words = []
    # При помощи цикла for переберите предполагаемо подходящие слова.
    low_root_word = root_word.lower()
    for i in other_words:
        low_other_word = i.lower()
        # Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий
        # список same_words.
        if (low_root_word in low_other_word) or (low_other_word in low_root_word):
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
#
# Файл с кодом (module_2_6.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий
# с файлом решения.
