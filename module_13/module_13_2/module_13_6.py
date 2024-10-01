# Домашнее задание по теме "Инлайн клавиатуры".
# Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Ещё больше выбора":
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '==  Ваш API  =='
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
kb.row(calculate_button, info_button)
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
inline_menu = InlineKeyboardMarkup(resaze_keyboard=True)
b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
b2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_menu.row(b1, b2)



# По итогу получится следующий алгоритм:
# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
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
    :param message:
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
async def send_colories(message, state):
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
    :param message:
    :param state:
    :return:
    """
    await state.update_data(weight=message.text)
    data = await state.get_data()
    colories = 10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) + 5
    await message.answer(f'Ваша норма колорий: {colories}')
    # Финишируйте машину состояний методом finish().
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, что бы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
#
# Пример результата выполнения программы:
#
#
#
# Примечания:
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
# Файл module_13_6.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
