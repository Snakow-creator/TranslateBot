import random

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import apps.handlers as h
import apps.keyboards as kb


async def win_or_lose(win) -> str:
    if win:
        return random.choice(win_list)
    else:
        return random.choice(lose_list)


async def win(user_id, state: FSMContext, win: bool = True) -> str:
    await state.clear()
    text_word = h.word.get(user_id)
    text = f"<b>{text_word[0]}</b> = "
    for n in range(1, len(text_word)):
        text += f"{text_word[n]}, "

    if win:
        discription = await win_or_lose(True)
    else:
        discription = await win_or_lose(False)

    return f"{discription} {text[0:-2]}."


async def win_phrase(user_id, state: FSMContext, win: bool = True) -> str:
    await state.clear()
    text_word = h.word.get(user_id)
    text = f"<b>{text_word[0]}</b> = "
    discription = await win_or_lose(True)
    for n in range(1, len(text_word)):
        if (type(text[n])) == list:
            continue
        text += f"{text_word[n]}, "

    if win:
        discription = await win_or_lose(True)
    else:
        discription = await win_or_lose(False)

    return f"{discription} {text[0:-2]}."


async def check_phrase(message: Message, text_user) -> bool | None:
    text_word = h.word.get(message.from_user.id)
    if text_user in text_word:
        return True
    elif type(text_word[-1]) is list:
        if text_user in text_word[-1]:
            return True


win_list = [
    "Правильно! \nОтвет: ",
    "Ты совершенно прав! \nОтвет: ",
    "Это верно! \nОтвет: ",
]
lose_list = [
    "Ты не угадал! \nПравильный ответ:",
    "Это не верно. \nПравильный ответ:",
    "Неправильно. \nПравильный ответ:",
]
