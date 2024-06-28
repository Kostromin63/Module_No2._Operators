# Дополнительное практическое задание по модулю*
# Дополнительное практическое задание по модулю: "Подробнее о функциях."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
#
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Все ученики урбана, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются
# в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже
# после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин
# всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких
# структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
#
# Выходные данные (консоль):
# 99
#
#
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

def calculate_structure_sum(data_structure):

    # data_ = data_structure
    structure_length = len(data_structure)

    for i in data_structure:
    #next_element = None #data_[0]


        if isinstance(i, list):
        #     # Разберем список
            structure_length = len(data_structure)
            if len(i) <= 1:
                return next_element
            #next_element = data_structure[0]
            return calculate_structure_sum(data_structure[0])
        # elif isinstance(data_structure, tuple):
        # #     # Разберем кортеж
        #     #next_element = data_[0]
        #     if len(next_element) <= 1:
        #         return next_element
        #     return calculate_structure_sum(next_element[1:])
        # elif isinstance(data_structure, dict):
        # #     # Разберем
        #     #next_element = data_[0]
        #     if len(next_element) <= 1:
        #         return next_element
        #     return calculate_structure_sum(next_element[1:])
        elif isinstance(data_structure, int):
            next_element = data_structure

            return next_element
        print(data_)
        print(type(data_))
        print(next_element)
        print(type(next_element))
    # print(next_)
    # print(type(next_))
    # print(next2)
    # print(type(next2))
#    return 123
    return str(next_element) + calculate_structure_sum(data_[1:])

#data_structure = [[]]
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# data_structure = 1
result = calculate_structure_sum(data_structure)
print(result)
