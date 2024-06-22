# Самостоятельная работа по уроку "Рекурсия"
#
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение
# цифр этого числа.
#
# Пункты задачи:
# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)
    # Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
    # из str_number в числовом представлении(int).
    first = int(str_number[0])
    if len(str_number) <= 1:
        # result_of_multiplication = result_of_multiplication * first
        return first
    # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру
    # числа на результат работы этой же функции с числом, но уже без первой цифры.
    # result_of_multiplication = first * get_multiplied_digits(int(str_number[1:]))
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
