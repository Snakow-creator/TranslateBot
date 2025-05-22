import random

from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import apps.handlers as h
import apps.keyboards as kb
from apps.functions import win, win_phrase
from base.lite_translate import translate
from base.phrase_translate import ph_translate

word = {}
router = Router()


@router.callback_query(F.data == "lite_repeat")
async def lite_translate_repeat(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(h.Translate.us)
    h.num[callback.from_user.id] = 0
    index = random.randint(0, (len(translate) - 1))
    h.word[callback.from_user.id] = translate[index]
    text_word = h.word.get(callback.from_user.id, [])
    await callback.message.edit_text(
        f"Выпало слово: <b>{text_word[0]}</b>.\nНапишите правильный перевод:",
        reply_markup=kb.translate_cancel("lite"),
    )


@router.callback_query(F.data == "phrase_repeat")
async def phrase_translate_repeat(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(h.Translate.us_phrase)
    h.num[callback.from_user.id] = 0
    index = random.randint(0, (len(ph_translate) - 1))
    h.word[callback.from_user.id] = ph_translate[index]
    text_word = h.word.get(callback.from_user.id, [])
    await callback.message.edit_text(
        f"Выпало фраза: <b>{text_word[0]}</b>.\nНапишите правильный перевод:",
        reply_markup=kb.translate_cancel("phrase"),
    )


@router.callback_query(F.data == "lite_cancel")
async def cancel_lite_translate(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    text = await win(callback.from_user.id, state, win=False)
    await callback.message.edit_text(text, reply_markup=kb.repeat_keyboard("lite"))


@router.callback_query(F.data == "phrase_cancel")
async def cancel_phrase_translate(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    text = await win_phrase(callback.from_user.id, state, win=False)
    await callback.message.edit_text(text, reply_markup=kb.repeat_keyboard("phrase"))
