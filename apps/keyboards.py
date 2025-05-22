import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Простой перевод🇺🇸"),
            KeyboardButton(text="Перевод фраз🦜"),
        ],
        [KeyboardButton(text="Информацияℹ️")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Нажмите на кнопку ниже.",
)


def translate_cancel(action):
    text_list = ["Я не знаю🫨", "Я не помню😵‍💫", "Я забыл😖"]
    text = random.choice(text_list)
    button = [[InlineKeyboardButton(text=f"{text}", callback_data=f"{action}_cancel")]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def repeat_keyboard(action):
    text_list = ["Ещё разок🔄", "Попробовать еще раз🔁", "Повторить🔄"]
    text = random.choice(text_list)
    button = [[InlineKeyboardButton(text=text, callback_data=f"{action}_repeat")]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
