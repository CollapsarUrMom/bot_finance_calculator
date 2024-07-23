from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from kbds import user_kbds


user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет пока что я умею только обрабатывать текст, вызови команду меню')


@user_router.message(Command('menu'))
async def user_menu(message: types.Message):
    await message.answer('Это то что я умею', reply_markup= user_kbds.menu_kb)