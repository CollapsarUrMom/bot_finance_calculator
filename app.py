# Итак, ты сделал копию репозитория чтоб, создать виртуальное окружение, как я понимаю тебе надо установить питон,
# или ты его уже устанавливал? в VS Code думаю там всё есть

# Возможно будет ругаться PowerShell тогда надо ввести это (под правами администратора)

# Set-ExecutionPolicy Unrestricted

# Что бы отключить эту настройку нужно ввести
# Set-ExecutionPolicy Restricted
# Это будет стандартная настройка Powershell

# Чтоб ты мог создавать виртуальные окружения тебе нужна прога, в терминале введи команду pip install virtualenv всё скачается

# Создавать виртуальное окружение не надо так как на Git уже он есть. Папка env

# Теперь нужно активировать вирт. окр.(env)
# введи команду env\Scripts\activate

# Введи команду pip list у тебя должен терминал выдать установленные библиотеки как в requirements.txt

# Либо pip freeze, а потом pip freeze >requirements.txt. Должны закачаться все нужные библиотеки

# Всё это я сделал на компе и это работает, а на ноуте не хочет. Если у тебя заработает, то это трабла ноута и я буду разбираться

# Ниже ещё команды это я для себя уже сделал

# ====================================================================


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