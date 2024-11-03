# Домашнее задание по теме "Модели данных Pydantic"
#
# Цель: научиться описывать и использовать Pydantic модель.
#
# Задача "Модель пользователя":
# Подготовка:
# Используйте CRUD запросы из предыдущей задачи.
# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Цель: выработать навык работы с CRUD запросами.
#
# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()


# Создайте пустой список users = []
users = []


# Создайте класс(модель) User, наследованный от BaseModel
class User(BaseModel):
    """
    Класс будет содержать следующие поля:
    id - номер пользователя (int)
    username - имя пользователя (str)
    age - возраст пользователя (int)
    """
    id: int = None
    username: str = None
    age: int = None

# Измените и дополните ранее описанные 4 CRUD запроса:
# get запрос по маршруту '/users' теперь возвращает список users.
#
# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.
#
# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
#
# delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.


@app.get('/')
async def welcom() -> str:
    return 'Welcom!!'


@app.get('/users')
async def get_users() -> List[User]:
    """
    get запрос по маршруту '/users' теперь возвращает список users.
    :return:
    """
    return users


@app.post('/user/{username}/{age}')
async def user_registration(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Vasiliy')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=75)]
        ) -> User:
    """
    post запрос по маршруту '/user/{username}/{age}', теперь:
    Добавляет в список users объект User.
    id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
    Все остальные параметры объекта User - переданные в функцию username и age соответственно.
    В конце возвращает созданного пользователя.
    :param username:
    :param age:
    :return:
    """
    if any(users):
        next_index = max(users, key=lambda us: us.id).id + 1
        # next_index = max(users, key=id).id + 1
    else:
        next_index = 1
    user = User(id=next_index, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=125)],
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Vasiliy')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=75)]
        ):
    """
    Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
    В случае отсутствия пользователя
    выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
    :param user_id:
    :param username:
    :param age:
    :return:
    """
    user_wrapped_in_a_sheet = list(filter(lambda us: us.id == user_id, users))  # голубец :)
    if any(user_wrapped_in_a_sheet):
        user = user_wrapped_in_a_sheet[0]
        user.id = user_id
        user.username = username
        user.age = age
        return user
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=125)]
        ) -> User:

    user_wrapped_in_a_sheet = list(filter(lambda us: us.id == user_id, users))  # голубец :)
    if any(user_wrapped_in_a_sheet):
        user = user_wrapped_in_a_sheet[0]
        index_delete = users.index(user)
        users.pop(index_delete)
        return user
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/')
async def delete_all_user() -> str:
    users.clear()
    return "Все записи о пользователях удалены."


# Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
# 1. GET '/users'
#
# # 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
#
# # 3. POST '/user/{username}/{age}' # username - UrbanTest, age - 36
#
# # 4. POST '/user/{username}/{age}' # username - Admin, age - 42
#
# # 5. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
#
# 6. DELETE '/user/{user_id}' # user_id - 2
#
# 7. GET '/users'
#
# 8. DELETE '/user/{user_id}' # user_id - 2
#
#
#
# Файл module_16_4.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
