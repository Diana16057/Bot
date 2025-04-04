from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from termcolor import colored
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Хэндлер на команду /comands
@router.message(Command("comands"))
async def cmd_comands(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Основные команды")],
        [types.KeyboardButton(text="Трюковые команды")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите раздел команды"
    )
    await message.answer("С каких команд хотите начать обучение?", reply_markup=keyboard)
# Хэндлер на кнопки /comands
@router.message(F.text.lower() == "основные команды")
async def basic_commands(message: types.Message):
    content = Text(
        'Молодец! Все верно! Обучение именно с этого нужно начинать! Вот несколько команд и рекомендации по их обучению:\n ', 
        Bold('Сидеть. '), 'Нужно сказать «Сидеть» и мягко надавить на крестец, показывая, что нужно опуститься.\n'
        ' Другой рукой при этом нужно держать лакомство чуть выше головы пса, чтобы он не лёг полностью.\n'
        'Когда щенок сядет, нужно его похвалить и дать лакомство.\n',
        Bold('Лежать. '), 'После того как щенок сел, поднесите лакомство к его носу и в момент, когда он за ним потянется, произнесите команду «лежать».'
        ' Опустите руку вниз и вперёд, одновременно слегка надавливая на холку.'
        ' Если щенок послушался, поощрите его лакомством и похвалите оглаживанием, при этом повторите фразу: «хорошо, лежать».\n',
        Bold('Фу. '), 'Эта команда связана с наказанием, а не с наградой.\n'
        'Дрессировать лучше во время прогулки, как только щенок среагирует на что-то нежелательное, нужно строго сказать «Фу» и слегка натянуть поводок.\n',
        Bold('Ко мне. '), 'Такая команда не должна ассоциироваться с наказанием.'
        ' Для этого нужно подготовить что-нибудь приятное для питомца — игрушку или миску с кормом — и громко сказать «Ко мне».'
        'Когда щенок подойдёт, его нужно наградить тем, что у вас в руках, и похвалить.',  reply_markup=types.ReplyKeyboardRemove())
    await message.answer(
        **content.as_kwargs()) 
  
@router.message(F.text.lower() == "трюковые команды")
async def  trick_comands(message: types.Message):
    content2 = Text(
        "Если уже освоили основные команды, то можно приступать к трюкам!\n",
        Bold('Высокий прыжок. '), 'Нужно присесть на корточки, вытянуть перед питомцем ногу и продемонстрировать над «турником» приманку.'
        'Собака перепрыгнет через препятствие и получит поощрение. С каждым занятием ногу приподнимают выше.\n',
        Bold('Лови. '), 'Угощение держат на уровне глаз щенка — расстояние до морды около 1 м. Подкидывают лакомство вверх, приказывая «лови».'
        'Если животное поймает добычу, хорошо, когда не удалось — быстро прикрывают кусочек ладонью.\n',
        Bold('Кувырок. '), 'Собака ложится на пол. Рука с лакомством ведёт нос питомца к правому боку. '
        'Животное почувствует, что ему необходимо лечь на бок, что тут же и сделает. '
        'Продолжить заводить руку дальше, задача — заставить пса перевернуться на спину, а следом и на левый бок.\n',
        Bold('Тач. '), 'Смысл трюка — научить животное опираться передними лапами на руку хозяина или на поверхность. '
        'Расположить локоть хозяина на комфортной для собаки высоте. Угощением заставить её приподняться на задних лапах, а передними опереться на руку или поверхность.'
        'При правильном выполнении похвалить и отдать награду.', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(
        **content2.as_kwargs())