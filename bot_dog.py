import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, LinkPreviewOptions
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config_reader import config 
from handlers import start, horoscope, dog_breeds, hello, different_types, comands, help, recommendations #Импортируем хэндлеры на гороскоп и породы собак

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер   
dp = Dispatcher()
dp.include_routers(start.router,  horoscope.router, dog_breeds.router, hello.router, comands.router, help.router, recommendations.router, different_types.router)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot) 

if __name__ == "__main__":
    asyncio.run(main())


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(1)