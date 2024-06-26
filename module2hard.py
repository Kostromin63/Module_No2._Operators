# Дополнительное практическое задание по модулю*
# Дополнительное практическое задание по модулю: "Основные операторы"
#
# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали
# в ловушку местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными
# вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#
# К вашему счастью рядом с менее успешными и уже неговорящими путешествинниками находился попирус, где были написаны
# правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
#
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было
# кратно(делилось без остатка) сумме их значений.
#
# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)
#
#
# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
#
#
# К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движуться на вас
# (обожаю клише), тем более числа в первой вставке будут попадаться случайно.
#
# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа
# выдавала нужный пароль result, для одного введённого числа.
#


def get_password(first_field_of_stones):

    number_of_iterations = 1

    if 20 < first_field_of_stones < 3:
        print('Введите число больше 3, но меньше 20')
    elif first_field_of_stones % 2 == 0:
        number_of_iterations = first_field_of_stones // 2
    else:
        number_of_iterations = first_field_of_stones // 2 + 1

    my_password = ''

    for first_number_of_a_pair in range(1, number_of_iterations):

        for second_number_of_a_pair in range(1 + first_number_of_a_pair, first_field_of_stones):
            if first_field_of_stones % (first_number_of_a_pair + second_number_of_a_pair) == 0 \
                    and first_number_of_a_pair != second_number_of_a_pair:
                my_password = my_password + str(first_number_of_a_pair) + str(second_number_of_a_pair)

    return my_password


first_field_of_stones = int(input('Введите число от 3 до 20: '))
second_field_of_stones = get_password(first_field_of_stones)
print(second_field_of_stones)

# https://github.com/Kostromin63/Module_No2._Operators.git
# https://github.com/Kostromin63/Module_No2._Operators/blob/master/module2hard.py
