# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)

# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.
# Пример:
def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        simple = True

        if number < 2:
            print('Ни простое ни составное, а так себе')
        else:
            divider = 2
            for divider in range(divider, number):
                compound = number % divider == 0

                if compound:
                    simple = False
                    break
                divider += 1
            if simple:
                print('Простое')
            else:
                print('Составное')

        return number
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
#
# Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
print(sum_three(1, 2, 6))
print(sum_three(-5, 0, 0))
