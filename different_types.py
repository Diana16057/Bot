from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Это текстовое сообщение! Для работы используйте меню.")

@router.message(F.sticker)
async def echo_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)

@router.message(F.animation)
async def echo_gif(message: Message):
    await message.reply_animation(message.animation.file_id)
