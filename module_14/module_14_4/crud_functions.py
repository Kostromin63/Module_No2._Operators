# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db
# get_all_products
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
