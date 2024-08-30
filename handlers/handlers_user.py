from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import json

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
    await message.answer('Привет пока что я умею только обрабатывать текст, вызови команду меню',
                        reply_markup=get_keyboard(
                            'Добавить',
                            'Отмена',
                            placeholder=None,
                            sizes=(2,),
                        ))


@user_router.message(StateFilter(None), Command('snake'))
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


@user_router.message(StateFilter(None), Command('send_file'))
async def add_json(message: types.Message, state: FSMContext):
    await message.answer('Вставте файл')
    await state.set_state(Check_menu.input_document)


@user_router.message(Check_menu.input_document)
async def sendfile(message: types.document):
    await user_router.send_message(message.chat_id, "Send me the file")


# @user_router.message(F.document)
# async def a(message: types.Message):
#     await message.answer('Вижу файл!')
#     print(type(message.document))
#     await download_files(message.document)

@user_router.message(F.document)
async def get_document(message: types.Message):
    await message.answer('Вижу файл!')
    name = message.document.file_id #для уникальности файлов
    path = rf"C:\Users\Alex_job\Documents\Git\bot_finance_calculator\documents\{name}.json" #там создается папка documents, туда и будут сохраняться файлы
    await message.bot.download(destination_file=path)


    # file_info = await message.bot.get_file(message.document.file_id)
    # print(file_info)
    # file = await message.bot.download(file_info)
    # print(file)


    # file_info = await message.bot.get_file(message.document.file_id)
    # downloaded_file = await message.bot.download_file(destination= file_info.file_path)
    # print(downloaded_file)
    # with open("C:\\Users\\Alex_job\\Documents\\Git\\bot_finance_calculator\\extract.json", 'r', 'UTF-8') as file_object:
    #     print(file_object)
    #     await message.bot.send_message(message, f'Ваш  файл сохранен"')