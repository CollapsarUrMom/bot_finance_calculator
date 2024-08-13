from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from kbds.user_kbds import get_keyboard
from common import bot_common_list


user_router = Router()


class Snake_text(StatesGroup):
    text_input = State()



@user_router.message(Command('menu'))
@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет пока что я умею только обрабатывать текст, вызови команду меню',
                        reply_markup=get_keyboard(
                            'Добавить',
                            'Отмена',
                            placeholder='Вставте json',
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