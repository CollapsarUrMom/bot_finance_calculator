from aiogram import Router, types, F
from aiogram.types import CallbackQuery


callback_router = Router()


@callback_router.callback_query()
async def text_handler(call: CallbackQuery):
    await call.message.answer('Нажалась кнопка button1')