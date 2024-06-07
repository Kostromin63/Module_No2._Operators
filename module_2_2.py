#   Решение домашнего задания по уроку "Условная конструкция. Операторы if, elif, else."
#
#
# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел
# среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0
#
# Объявляем переменные и записываем в них значения:
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
# Создаем множество из 3х элементов и посмотрим количество уникальных значений в нем:
mynumbers = {first, second, third}
number_of_unique = len(mynumbers)
# сделаем соответствующие выводы:
if number_of_unique == 3:
    print(0)
elif number_of_unique == 2:
    print(2)
elif number_of_unique == 1:
    print(3)
else:
    print('Вы ввели не все значения. Пожалуйста повторите ввод всех трех значений')
# Код не совсем рабочий. Нет обработчика ошибок, если пользователь отказался от ввода какой нибудь цифры. Видимо
# передается Null(None) а пайтон, видимо, сам его преобразовать в 0 не может. Можно написать обработчик в отдельной
# функции и уже к нему обращаться для ввода значений. А можно и ограничить значения в поле ввода значений в
# пользовательской форме. Так как это пока не входит в рамки изучаемой темы, то с Вашего позволения, мы пока проппустим
# этот вопрос как есть и вернемся к нему в будущем.
