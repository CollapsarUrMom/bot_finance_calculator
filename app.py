# Чтобы актвировать виртуальное окружение нужно в Powershell ввести команду (под правами администратора)
# Set-ExecutionPolicy Unrestricted

# Что бы отключить эту настройку нужно ввести
# Set-ExecutionPolicy Restricted
# Это будет стандартная настройка Powershell

# Создание виртуального окружения
# python -m venv env

# Активация виртуального окружения
# env\Scripts\activate

# Установка пакетов в виртуальное окружение
# pip install starlette

# Удаление пакетов в виртуальном окружении
# pip uninstall starlette

# Деактивация виртуального окружения
# deactivate

# ====================================================================

import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это команда старт')


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())