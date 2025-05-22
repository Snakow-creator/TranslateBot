from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import apps.keyboards as kb
from apps.functions import win, win
from apps.functions import win_phrase, check_phrase
from base.lite_translate import translate
from base.phrase_translate import ph_translate
import random

router = Router()
word = {}
num = {}


class Translate(StatesGroup):
    us = State()
    us_phrase = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Приветствую {message.from_user.first_name}!"
        f"\nЭто бот переводчик Расл!"
        f"\nЯ переводчик английского!"
        f"\n\nНачать взаимодействие с ботом нажмите кнопку ниже⬇️",
        reply_markup=kb.main,
    )


@router.message(F.text == "Простой перевод🇺🇸")
async def us(message: Message, state: FSMContext):
    num[message.from_user.id] = 0
    await state.set_state(Translate.us)
    index = random.randint(0, (len(translate) - 1))  # выбираем случайный индекс
    word[message.from_user.id] = translate[index]  # выбираем случайный перевод слова
    text_word = word.get(message.from_user.id)  # достаем список из словаря
    await message.answer(
        f"Выпало слово: <b>{text_word[0]}</b>.\nНапишите правильный перевод:",
        reply_markup=kb.translate_cancel("lite"),
    )


@router.message(F.text == "Перевод фраз🦜")
async def phrase_translate(message: Message, state: FSMContext):
    num[message.from_user.id] = 0
    await state.set_state(Translate.us_phrase)
    index = random.randint(0, (len(ph_translate) - 1))  # выбираем случайный индекс
    word[message.from_user.id] = ph_translate[index]  # выбираем случайный перевод фразы
    text_word = word.get(message.from_user.id)  # достаем список из словаря
    await message.answer(
        f"Выпала фраза: <b>{text_word[0]}</b>.\nНапишите правильный перевод:",
        reply_markup=kb.translate_cancel("phrase"),
    )


@router.message(F.text == "Информацияℹ️")
async def information(message: Message):
    await message.answer(
        "Бот для перевода фраз с английского на русский.\n"
        "Расл: твой учитель английского!🤖",
        disable_web_page_preview=True,
    )


@router.message(Translate.us)
async def repeat(message: Message, state: FSMContext):
    text_user = message.text.lower()  # полученное слово переводим в нижний регистр
    text_word = word.get(message.from_user.id)
    num[message.from_user.id] += 1
    num_user = num.get(message.from_user.id, 0)
    if text_user in text_word:  # если есть слово в словаре то выдаем функцию выйгрыша
        text = await win(message.from_user.id, state)
        await message.answer(text, reply_markup=kb.repeat_keyboard("lite"))
    elif num_user == 3:  # если не угадывает то функцию проигрыша
        text = await win(message.from_user.id, state, win=False)
        await message.answer(text, reply_markup=kb.repeat_keyboard("lite"))
    else:  # если не одно из условий не соблюдается то отвечаем неверно
        await message.answer(
            "Неверно, попробуй еще раз.", reply_markup=kb.translate_cancel("lite")
        )


@router.message(Translate.us_phrase)
async def phrase_con(message: Message, state: FSMContext):
    text_user = message.text.capitalize()
    num[message.from_user.id] += 1
    num_user = num.get(message.from_user.id, 0)
    win = await check_phrase(message, text_user)
    if win:
        text = await win_phrase(message.from_user.id, state)
        await message.answer(text, reply_markup=kb.repeat_keyboard("phrase"))
    elif num_user == 3:
        text = await win_phrase(message.from_user.id, state, win=False)
        await message.answer(text, reply_markup=kb.repeat_keyboard("phrase"))
    else:
        await message.answer(
            "Неверно, попробуй еще раз.", reply_markup=kb.translate_cancel("phrase")
        )
