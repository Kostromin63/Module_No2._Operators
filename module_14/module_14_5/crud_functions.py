# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
# initiate_db
# add_user(username, email, age)
# is_included(username)
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#

import sqlite3 as sq


def connect_to_db():
    connection = sq.connect('not_telegram.db')
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection):
    connection.commit()
    connection.close()


def initiate_db():
    """
    Создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
    Эта таблица должна содержать следующие поля:
    id - целое число, первичный ключ
    title(название продукта) - текст (не пустой)
    description(описание) - тест
    price(цена) - целое число (не пустой)

    дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
    Эта таблица должна содержать следующие поля:
    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число (не пустой)
    balance - целое число (не пустой)
    :return:
    """

    params_conn = connect_to_db()
    params_conn[1].execute(
        """
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NON NULL,
        description TEXT,
        price INTEGER NON NULL)
        """
    )
    close_connection(params_conn[0])

    params_conn = connect_to_db()
    params_conn[1].execute(
        """
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NON NULL,
        email TEXT NOT NULL,
        age INTEGER NON NULL,
        balance INTEGER NON NULL)
        """
    )
    close_connection(params_conn[0])


def get_all_products():
    """
    возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
    :return:
    """
    params_conn = connect_to_db()
    params_conn[1].execute(
        """
        SELECT * FROM Products
        """
    )

    result = params_conn[1].fetchall()
    close_connection(params_conn[0])

    return result


def add_products(products):
    params_conn = connect_to_db()
    for product in products:
        params_conn[1].execute(
            """INSERT INTO Products (title, description, price) VALUES (?, ?, ?)""",
            (product[0], product[1], product[2])
        )

    close_connection(params_conn[0])


def add_user(username, email, age, balance=1000):
    """
    принимает: имя пользователя, почту и возраст. Данная функция должна добавлять
    в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000.
    Для добавления записей в таблице используйте SQL запрос.
    :param username:
    :param email:
    :param age:
    :return:
    """
    params_conn = connect_to_db()
    params_conn[1].execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (username, email, age, balance)
    )

    close_connection(params_conn[0])


def is_included(username):
    """
    принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users, в
    противном случае False. Для получения записей используйте SQL запрос
    :param username:
    :return:
    """
    params_conn = connect_to_db()
    params_conn[1].execute(
        "SELECT * FROM Users WHERE username = ?",
        (username,)
    )

    result = params_conn[1].fetchall()
    close_connection(params_conn[0])

    return len(result)

# initiate_db()
# products = [
#     ("burgeg", 'Мини Тести', 60),
#     ("cake", "Бисквитный трайфл", 270),
#     ("coca-cola", "Просто Cola", 52),
#     ("donut", 'Пончик "Сладость"', 23),
#     ("donut witg filing", "Пончик с малиной", 32),
#     ("ice cream", "Мороженое с ежевикой", 50),
#     ("lemon juice", "Сок лимона", 250),
#     ("rolls", "Сальмон ролл", 280)
# ]
# add_products(products)
# print(get_all_products())
