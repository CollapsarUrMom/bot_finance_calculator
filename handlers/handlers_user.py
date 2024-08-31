from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.methods import GetFile
from aiogram.types import URLInputFile
import json
import os

from sqlalchemy.ext.asyncio import AsyncSession

from kbds.user_kbds import get_keyboard
from common import bot_common_list
from database.models import Product
from database.json_query import download_files



user_router = Router()


class Snake_text(StatesGroup):
    text_input = State()


class Check_menu(StatesGroup):
    input_document = State()



@user_router.message(Command('menu'))
@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, выбери команду',
                        reply_markup=get_keyboard(
                            'Пополнить базу данных',
                            'Отмена',
                            placeholder=None,
                            sizes=(2,),
                        ))


@user_router.message(StateFilter(None), Command('snake_text'))
async def task_formation(message: types.Message, state: FSMContext):
    await state.set_state(Snake_text.text_input)
    await message.answer('Вставте необходимый текст')


@user_router.message(Snake_text.text_input)
async def func_input_text(message: types.Message, state: FSMContext):
    await state.update_data(input_text= message.text)
    await message.answer(await bot_common_list.revers_text(await state.get_data()))
    await state.clear()


@user_router.message(F.text == 'Отмена')
async def func_input_text(message: types.Message, state: FSMContext):
    await message.answer('Сработал', reply_markup=types.ReplyKeyboardRemove())


@user_router.message(StateFilter(None), Command('add_file'))
async def add_json(message: types.Message, state: FSMContext):
    await message.answer('Вставте файл')
    await state.set_state(Check_menu.input_document)


@user_router.message(Check_menu.input_document)
async def sendfile(message: types.Message, state: FSMContext):
    file = await message.bot.get_file(file_id= message.document.file_id)
    await message.bot.download_file(file_path= file.file_path, destination= 'Check12.json')
    await state.clear()