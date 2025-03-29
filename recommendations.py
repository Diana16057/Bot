import random
from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import choice

router = Router()

rec = ['Правильно обустройте пространство',
        'Не пренебрегайте прогулками',
        'Обзаведитесь правильными контактами',
        'Выберите качественное питание',
        'Не забывайте про дрессировку',
        'Не очеловечивайте собаку',
        'Не кормите едой со стола',
        'Будьте готовы к периоду адаптации',
        'Будьте последовательны в своих действиях',
        'Дарите внимание и заботу']

#Хэндлер на команду рандом
@router.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Советы собачникам",
        callback_data="random_choice")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил совет",
        reply_markup=builder.as_markup()
    )
@router.callback_query(F.data == "random_choice")
async def send_random_choice(callback: types.CallbackQuery):
    await callback.message.answer(str(random.choice(rec)))