from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обработчик текста', callback_data='button1')],
    [InlineKeyboardButton(text='В разработке!', callback_data='button2')]
]
)
