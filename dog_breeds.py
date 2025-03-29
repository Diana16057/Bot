from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

router = Router()

# Хэндлер на инлан-кнопки /породы собак
@router.message(Command("dog_breeds_url"))
async def cmd_dog_breedsl_url(message: types.Message):
    builder = InlineKeyboardBuilder() 
    builder.row(types.InlineKeyboardButton(
        text="Хаски 🐺", url="https://lapkins.ru/dog/sibirskiy-khaski")
    )  
    builder.row(types.InlineKeyboardButton(
        text="Мопс", url="https://lapkins.ru/dog/mops")
    )  
    builder.row(types.InlineKeyboardButton(
        text="Немецкая овчарка", url="https://lapkins.ru/dog/nemetskaya-ovcharka")
    )  
    builder.row(types.InlineKeyboardButton(
        text="Лабрадор-ретривер", url="https://lapkins.ru/dog/labrador-retriver")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Французские бульдоги", url="https://lapkins.ru/dog/frantsuzskiy-buldog")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Пудель 🐩", url="https://lapkins.ru/dog/pudel")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Вельш-корги пемброк", url="https://lapkins.ru/dog/velsh-korgi-pembrok")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Джек-рассел-терьер", url="https://lapkins.ru/dog/dzhek-rassel-terer")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Йоркширский терьер", url="https://lapkins.ru/dog/yorkshirskiy-terer")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Доберман", url="https://lapkins.ru/dog/doberman")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Померанский шпиц", url="https://lapkins.ru/dog/pomeranskiy-shpits")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Ротвейлер", url="https://lapkins.ru/dog/rotveyler")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Акита-ину", url="https://lapkins.ru/dog/akita-inu")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Русский той-терьер", url="https://lapkins.ru/dog/russkiy-toy-terer/")
    ) 
    builder.row(types.InlineKeyboardButton(
        text="Бордер-колли", url="https://lapkins.ru/dog/border-kolli")
    )                 

    await message.answer(
         '15 Популярных пород собак',
        reply_markup=builder.as_markup(),
    )