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
from aiogram import Bot, Dispatcher

from dotenv import find_dotenv, load_dotenv

from handlers.handlers_user import user_router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


dp.include_router(user_router)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())