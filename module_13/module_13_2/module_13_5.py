# Домашнее задание по теме "Клавиатура кнопок".
# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались
# по нажатию кнопки.
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = '==  Ваш api  =='
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать'
# и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи
# параметра resize_keyboard.
kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
kb.row(calculate_button, info_button)


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


# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать',
# а не на 'Calories'.
@dp.message_handler(text='Рассчитать')
async def set_age(message):
    """
     Функцию set_age(message):
    Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
    Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
    :param message:
    :return:
    """
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

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
# Клавиатура по команде /start:
#
# После нажатия на кнопку 'Рассчитать':
#
#
# Примечания:
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
# Файл module_13_5.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
