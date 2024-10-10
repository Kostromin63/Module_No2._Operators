# Домашнее задание по теме "Доработка бота"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: подготовить Telegram-бота для взаимодействия с базой данных.
#
# Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.
#
# Дополните ранее написанный код для Telegram-бота:
#
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".

kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
buy_button = KeyboardButton(text='Купить')
kb.row(calculate_button, info_button)
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

# По итогу получится следующий алгоритм:
# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать', 'Информация' и 'Купить'.
# В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
# По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
# По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.


# Создайте класс UserState наследованный от StateGroup.
class UserState(StatesGroup):
    """
    Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
    Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов.
    """
    age = State()
    growth = State()
    weight = State()
    gender = State()


# Создайте хэндлеры и функции к ним:
#
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number>
# | Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
#

@dp.message_handler(text='Купить')
async def get_buying_list(message):

    for i in range(1, 5):
        await message.answer(f"Product{i} | Описание: описание {i} | Цена: {i*100}")
        with open(f'photos/{i}.png', 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_menu_buy)

# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        'Для женщин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) − 161.'
        ' Для мужчин: (10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) + 5.')
    await call.answer()


# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
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

# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью
# 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.


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


# @dp.callback_query_handler(**('male', 'female'))
# @dp.callback_query_handler(lambda text: text=="male" or text=="female")
# @dp.callback_query_handler(lambda text: text in ["male", "female"])
# @dp.callback_query_handler(lambda c: c.data == "male" or c.data == "female")
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

# Примечания:
# Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)
# Файл module_14_3.py с кодом загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
