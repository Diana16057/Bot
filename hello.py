from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold

router = Router()

# Хэндлер на команду /hello
@router.message(Command("hello"))
async def cmd_hello(message: types.Message):
      content = Text(
        "Привет, ",
        Bold(message.from_user.full_name))
      await message.answer(
        **content.as_kwargs())