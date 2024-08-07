from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from kbds import user_kbds
from common import bot_common_list


user_router = Router()


class Text_handler(StatesGroup):
    text_input = State()



@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет пока что я умею только обрабатывать текст, вызови команду меню')


@user_router.message(Command('menu'))
async def user_menu(message: types.Message):
    await message.reply('Это то что я умею', reply_markup= user_kbds.menu_kb)
    print('Появилась клавиатура')


@user_router.message(F.text == 'new')
async def user_menu(message: types.Message):
    await message.reply('Заработало!')


@user_router.message(StateFilter(None), F.text == 'Er')
async def task_formation(message: types.Message, state: FSMContext):
    await state.set_state(Text_handler.text_input)
    await message.answer('Вставте необходимый текст')


@user_router.message(Text_handler.text_input, F.text)
async def func_input_text(message: types.Message, state: FSMContext):
    await state.update_data(input_text= message.text)
    await message.answer(await bot_common_list.revers_text(await state.get_data()))
    await state.clear()
