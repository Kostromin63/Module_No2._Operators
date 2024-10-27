# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Цель: выработать навык работы с CRUD запросами.
#
# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
users = {'1': 'Имя: Example, возраст: 18'}


# Реализуйте 4 CRUD запроса:
# 1
@app.get('/users')
async def get_users() -> dict:
    """
    get запрос по маршруту '/users', который возвращает словарь users.
    :return:
    """
    return users


# 2
@app.post('/user/{username}/{age}')
async def user_registration(
                    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
                    ) -> str:
    """
    post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом
    значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
    :param username:
    :param age:
    :return:
    """
    next_index = str(int(max(users, key=int)) + 1)
    users[next_index] = f'Имя: {username}, возраст {age}'
    return f'User {next_index} is registered'


# 3
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
                    user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter User ID')],
                    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
                    ) -> str:
    """
    put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом
    user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is registered"
    :param user_id:
    :param username:
    :param age:
    :return:
    """
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'


# 4
@app.delete('/user_id')
async def delete_user(
                    user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter User ID')]
                    ) -> str:
    users.pop(user_id)
    """
    delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару."""
    return f'User {user_id} has been deleted'

# Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
# 1. GET '/users'
# {
# "1": "Имя: Example, возраст: 18"
# }
# 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
# "User 2 is registered"
# 3. POST '/user/{username}/{age}' # username - NewUser, age - 22
# "User 3 is registered"
# 4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
# "User 1 has been updated"
# 5. DELETE '/user/{user_id}' # user_id - 2
# "User 2 has been deleted"
# 6. GET '/users'
# {
# "1": "Имя: UrbanProfi, возраст: 28",
# "3": "Имя: NewUser, возраст: 22"
# }
# Пример результата выполнения программы:
# Как должен выглядеть Swagger:
#
#
# Примечания:
# Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.
# Файл module_16_3.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
