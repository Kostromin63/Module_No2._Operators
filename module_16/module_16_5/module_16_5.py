# Домашнее задание по теме "Шаблонизатор Jinja 2."
#
# Цель: научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах.
#
# Задача "Список пользователей в шаблоне":
# Подготовка:
# Используйте код из предыдущей задачи.
# Скачайте заготовленные шаблоны для их дополнения.
# Шаблоны оставьте в папке templates у себя в проекте.
#

from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Создайте объект Jinja2Templates, указав в качестве папки шаблонов - templates.
#

templstes = Jinja2Templates(directory="templates")

users = []


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


# Измените и дополните ранее описанные CRUD запросы:
# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request
# и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
# Измените get запрос по маршруту '/user' на '/user/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request
# и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
#
@app.get('/')
async def main_page(request: Request) -> HTMLResponse:
    """
    Напишите новый запрос по маршруту '/':
    Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
    TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request
    и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
    :return:
    """
    return templstes.TemplateResponse('users.html', {'request': request, 'users': users})


# @app.get('/users')
# async def get_users() -> list:
#     return users


@app.get('/user/{user_id}')
async def get_user(request: Request,
                   user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=2)]) -> HTMLResponse:
    """
    Измените get запрос по маршруту '/user' на '/user/{user_id}':
    Функция по этому запросу теперь принимает аргумент request и user_id.
    Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
    TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request
    и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
    :return:
    """
    user_wrapped_in_a_sheet = list(filter(lambda us: us.id == user_id, users))  # голубец :)
    try:
        user = user_wrapped_in_a_sheet[0]
        return templstes.TemplateResponse('users.html', {'request': request, 'user': user})
    except IndexError:
        raise HTTPException(status_code=404, detail='user was not found')


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=2)]
) -> str:
    user_wrapped_in_a_sheet = list(filter(lambda us: us.id == user_id, users))  # голубец :)
    try:
        user = user_wrapped_in_a_sheet[0]
        index_delete = users.index(user)
        users.pop(index_delete)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


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
    try:
        user = user_wrapped_in_a_sheet[0]
        user.id = user_id
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# Создайте несколько пользователей при помощи post запроса со следующими данными:
# username - UrbanUser, age - 24
# username - UrbanTest, age - 22
# username - Capybara, age - 60
# def create_3users():
#     user = User(id=1, username='UrbanUser', age=24)
#     users.append(user)
#     user = User(id=2, username='UrbanTest', age=22)
#     users.append(user)
#     user = User(id=3, username='Capybara', age=60)
#     users.append(user)


# create_3users()
# В шаблоне 'users.html' заготовлены все необходимые теги и обработка условий, вам остаётся только дополнить
# закомментированные строки вашим Jinja 2 кодом (использование полей id, username и age объектов модели User):
# 1. По маршруту '/' должен отображаться шаблон 'users.html' со списком все ранее созданных объектов:
#
# 2. Здесь каждая из записей является ссылкой на описание объекта,
# информация о котором отображается по маршруту '/user/{user_id}':
#
# Файл module_16_5.py, шаблоны main.html и users.html загрузите на ваш GitHub репозиторий.
# В решении пришлите ссылку на него.
# Успехов!
