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
from aiogram import Bot, Dispatcher, types

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from common.bot_common_list import private
from handlers.handlers_user import user_router
from middlewares.db import DataBaseSession
from database.engine import create_db, drop_db, session_maker



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_router)

async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()

async def on_shutdown(bot):
    print('бот лег')



async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True) # Сброс ожидаемых обновлений
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) # Удаление кнопки меню
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats()) # Сама кнопка меню
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

asyncio.run(main())