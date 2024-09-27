# Домашнее задание по теме "Методы отправки сообщений".
# Цель: написать простейшего телеграм-бота, используя асинхронные функции.
#
# Задача "Он мне ответил!":
# Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
# Запустите ваш Telegram-бот и проверьте его на работоспособность.
# Пример результата выполнения программы:
#
# Примечания:
# Для ответа на сообщение запускайте метод answer асинхронно.
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
# Файл module_13_3.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
#
# Из за проблем совместимости реализовано на версии Python 3.9
#

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '== ЗДЕСЬ НАДО ВСТАВИТЬ РЕАЛЬНЫЙ КЛЮЧ ВАШЕГО БОТА =='
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print("Urban message")


@dp.message_handler(commands=['start'])
async def start(message):
    print("Start message")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    print(f'Мы получили сообщение "{message["text"]}" от пользователя "{message["from"]["username"]}"')
    await message.answer("Введите команду /start, что бы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
