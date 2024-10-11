# Домашнее задание по теме "Написание примитивной ORM"
#
# Цель: написать простейшие CRUD функции для взаимодействия с базой данных.
#
# Задача "Регистрация покупателей":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
# initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число (не пустой)
# balance - целое число (не пустой)
# add_user(username, email, age), которая принимает: имя пользователя, почту и возраст. Данная функция должна добавлять
# в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000. Для добавления
# записей в таблице используйте SQL запрос.
# is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
# в противном случае False. Для получения записей используйте SQL запрос.
#
# Изменения в Telegram-бот:
# Кнопки главного меню дополните кнопкой "Регистрация".
# Напишите новый класс состояний RegistrationState с следующими объектами класса
# State: username, email, age, balance(по умолчанию 1000).
# Создайте цепочку изменений состояний RegistrationState.
# Фукнции цепочки состояний RegistrationState:
# sing_up(message):
# set_username(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
# Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text.
# Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
# Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и
# запрашивать новое состояние для RegistrationState.username.
# set_email(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
# Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
# Далее выводить сообщение "Введите свой возраст:":
# После ожидать ввода возраста в атрибут RegistrationState.age.
# set_age(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
# Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
# Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users
# при помощи ранее написанной crud-функции add_user.
# В конце завершать приём состояний при помощи метода finish().
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.
#

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import get_all_products, is_included, add_user

api = 'API'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".

kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
buy_button = KeyboardButton(text='Купить')
reg_button = KeyboardButton(text='Регистрация')
kb.row(calculate_button, info_button, reg_button)
kb.add(buy_button)

inline_menu = InlineKeyboardMarkup(resaze_keyboard=True)
b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
b2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_menu.row(b1, b2)

gender_selection_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мужской', callback_data='male'),
            InlineKeyboardButton(text='Женский', callback_data='female')
        ]
    ], resaze_keyboard=True
)

# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"

inline_menu_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    """
    Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
    Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов.
    """
    age = State()
    growth = State()
    weight = State()
    gender = State()


class RegistrationState(StatesGroup):
    """
    State: username, email, age, balance(по умолчанию 1000).
    """
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    """
    Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
    Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
    После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
    :param message:
    :return:
    """
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    """
    Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
    Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text.
    Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
    Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и
    запрашивать новое состояние для RegistrationState.username.
    :param message:
    :param state:
    :return:
    """
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('"Пользователь существует, введите другое имя"')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    """
    Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
    Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
    Далее выводить сообщение "Введите свой возраст:":
    После ожидать ввода возраста в атрибут RegistrationState.age.
    :param message:
    :param state:
    :return:
    """
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    """
    Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
    Эта функция должна обновлять данные в состоянии RegistrationState.age на message.text.
    Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users
    при помощи ранее написанной crud-функции add_user.
    В конце завершать приём состояний при помощи метода finish().
    :param message:
    :param state:
    :return:
    """
    await state.update_data(age=message.text)
    # await state.update_data(balance=1000)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно.')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    all_products = get_all_products()
    for product in all_products:
        await message.answer(f"{product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        with open(f'photos/{product[1]}.png', 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_menu_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        'Для женщин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) − 161.'
        ' Для мужчин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) + 5.')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    """
     Функцию set_age(message):
    Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
    Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
    :param :
    :return:
    """
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    """
    Функцию set_growth(message, state):
    Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
    Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
    После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
    :param message:
    :param state:
    :return:
    """
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    """
    Функцию set_weight(message, state):
    Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
    Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
    После ожидать ввода веса в атрибут UserState.weight при помощи метода set.
    :param message:
    :param state:
    :return:
    """
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    """
    Введем состояние = пол (gender)
    :param message:
    :param state:
    :return:
    """
    await state.update_data(weight=message.text)
    await message.answer('Выбрать пол', reply_markup=gender_selection_kb)
    await UserState.gender.set()


@dp.callback_query_handler(state=UserState.gender)
async def send_colories(call, state):
    """
    Функцию send_calories(message, state):
    Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
    Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
    Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин -
    на ваше усмотрение). Данные для формулы берите из ранее объявленной переменной data по ключам age,
    growth и weight соответственно.
    Формула Миффлина — Сан-Жеора выглядит так:
    Для женщин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) − 161.
    Для мужчин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) + 5.
    Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
    :param call:
    :param :
    :param state:
    :return:
    """
    await UserState.gender.set()
    await state.update_data(gender=call.data)
    data = await state.get_data()
    if data['gender'] == 'male':
        colories = 10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) + 5
        await call.message.answer(f'Ваша норма колорий: {colories}')
    elif data['gender'] == 'female':
        colories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
        await call.message.answer(f'Ваша норма колорий: {colories}')
    else:
        await call.message.answer(f'Ваш пол не определен.')
    # Финишируйте машину состояний методом finish().
    await call.answer()
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, что бы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


# Файлы module_14_5.py, crud_functions.py, а также файл с базой данных и таблицей Users загрузите на ваш GitHub
# репозиторий. В решении пришлите ссылку на него.
# Успехов!
