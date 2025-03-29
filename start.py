from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text

router = Router()

# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
      await message.answer(
            "Вас приветствует бот 'Собачник'🐕!\n"
            "Для работы с ботом воспользуйтесь кнопками Меню "
            "или командой /help"
      )