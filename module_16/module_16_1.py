# Домашнее задание по теме "Основы Fast Api и маршрутизация"
# Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI.
#
# Задача "Начало пути":
# Подготовка:
# Установите фреймворк FastAPI при помощи пакетного менеджера pip.
# Версию Python можете выбрать самостоятельно (3.9 - 3.12).
#
# Маршрутизация:
# Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
#
from fastapi import FastAPI

app = FastAPI()
# 2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".


@app.get('/')
async def home_page() -> dict:
    return {"message": "Главная страница"}

# 3.Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".


@app.get('/user/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как вдминистратор"}

# 4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".


@app.get('/user/{user_id}')
async def user_by_id(user_id: int = 0) -> dict:
    return {"message": f'Вы вошли как пользователь № {user_id}'}

# 5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
# http://127.0.0.1:8000/user?username=Alexandr&age=60


@app.get('/user')
async def user_info(username: str = 'user', age: int = 0) -> dict:
    return {"message": f"Инфформация о пользователе. Имя: {username}, Возраст: {age}"}

# Примечания:
# Все маршруты пишутся при мощи GET запроса.
# Помните о важности порядка записи запросов в вашем файле.
# Названия функций можете придумать самостоятельно с учётом логики прописанной в них.
# Файл module_16_1.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
