# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
#
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
#
# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.

# Код из предыдущего задания

import sqlite3 as sq

connection = sq.connect('module_14_1/not_telegram.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NON NULL
)
""")

# for i in range(1, 11):
#     cursor.execute(
#         "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#         (f'User{i}', f'example{i}@gmail.com', int(10)*i, '1000')
#     )

# for i in range(1, 11, 2):
#     cursor.execute(
#         "UPDATE Users SET balance = 500 WHERE id = ?",
#         (i,)
#     )

# for i in range(1, 11, 3):
#     cursor.execute(
#         "DELETE FROM Users WHERE id = ?",
#         (i,)
#     )

cursor.execute(
    "SELECT * FROM Users WHERE age != ?",
    (60,)
)

users_not60 = cursor.fetchall()
for user in users_not60:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute(
    "DELETE FROM Users WHERE ID = 6"
)

# Подсчитать общее количество записей.

cursor.execute(
    "SELECT COUNT(*) FROM Users"
)
total_users = cursor.fetchone()[0]

# Посчитать сумму всех балансов.

cursor.execute(
    "SELECT SUM(balance) FROM Users"
)
all_balances = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователя.

print(all_balances / total_users)

# Можно срелний баланс подсчитать в самом запросе

cursor.execute(
    "SELECT AVG(balance) FROM Users"
)
print(cursor.fetchone()[0])


connection.commit()
connection.close()

# Пример результата выполнения программы:
# Выполняемый код:

# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
#
# Вывод на консоль:
# 700.0
#
# Файл module_14_2.py с кодом и базу данных not_telegram.db загрузите на ваш GitHub репозиторий.
# В решении пришлите ссылку на него.
# Успехов!
