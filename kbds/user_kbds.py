from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




menu_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text='Обработка текста для чтения'),
        ],
        [
        KeyboardButton(text='В разработке')
        ],
    ],
    resize_keyboard= True,
    input_field_placeholder= 'Ну а что вы хотите!'
)