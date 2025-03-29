from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold

router = Router()

# Хэндлер на команду /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
      content = Text(
        "Что я умею?\n "
        "- Персонально здороваться /hello\n",
        "- Расcкажу о распространенных породах собак /dog_breeds_url\n",
        "- Вы можете узнать о характере вашей собаки по гороскопу /horoscope\n",
        "- Помогу обучить собаку командам /comands\n",
        "- Даю полезные советы собачникам /random\n",
        "- Умею пересылать гифки и стикеры",
        )
      await message.answer(
        **content.as_kwargs())