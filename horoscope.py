from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Хэндлер на команду гороскоп
@router.message(Command("horoscope"))
async def cmd_horoscope(message: types.Message):
    # Готовим кнопки
    button_oven = InlineKeyboardButton(text='Овен', callback_data='button_oven')
    button_telec = InlineKeyboardButton(text='Телец', callback_data='button_telec')
    button_bliznecy = InlineKeyboardButton(text='Близнецы', callback_data='button_bliznecy')
    button_rak = InlineKeyboardButton(text='Рак', callback_data='button_rak')
    button_lev = InlineKeyboardButton(text='Лев', callback_data='button_lev')
    button_deva = InlineKeyboardButton(text='Дева', callback_data='button_deva')
    button_vesy = InlineKeyboardButton(text='Весы', callback_data='button_vesy')
    button_scorpion = InlineKeyboardButton(text='Скорпион', callback_data='button_scorpion')
    button_strelec = InlineKeyboardButton(text='Стрелец', callback_data='button_strelec')
    button_kozerog = InlineKeyboardButton(text='Козерог', callback_data='button_kozerog')
    button_vodoley = InlineKeyboardButton(text='Водолей', callback_data='button_vodoley')
    button_ryby = InlineKeyboardButton(text='Рыбы', callback_data='button_ryby')
    # По очереди готовим текст и обработчик для каждого знака зодиака
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button_oven],[button_telec],
        [button_bliznecy],[button_rak],
        [button_lev],[button_deva],
        [button_vesy],[button_scorpion],
        [button_strelec],[button_kozerog],
        [button_vodoley],[button_ryby]]
        )
    resize_keyboard=True,
    await message.answer(
         'Выберите знак зодиака: ',
        reply_markup=keyboard
        )
    #Наполнение кнопок
@router.callback_query(F.data == "button_oven")
async def send_button_oven(callback: types.CallbackQuery):
    await callback.message.answer(text="Овен — первый знак гороскопа, поэтому неудивительно, что эти питомцы — прирожденные лидеры. Эти собаки — альфы, они любят движение и скорость.")
@router.callback_query(F.data == "button_telec")
async def send_button_telec(callback: types.CallbackQuery):
    await callback.message.answer(text="Можно описать Тельца одним словом: уютно! Рожденные весной, когда земля пышная и согретая солнцем, они чувственные, земные и естественные.")
@router.callback_query(F.data == "button_bliznecy")
async def send_button_bliznecy(callback: types.CallbackQuery):
    await callback.message.answer(text="Знак Близнецов, управляемый ментальным Меркурием, связан с общением, информацией и речью. Собаки-Близнецы обычно вокальные.")
@router.callback_query(F.data == "button_rak")
async def send_button_rak(callback: types.CallbackQuery):
    await callback.message.answer(text="Рак — водный знак, движимый эмоциями, а не логикой, что делает их чувствительными, сострадательными и интуитивными. Рожденные, когда солнце в зените, они обладают тихой, но внутренней силой и движутся в собственном ритме. ")
@router.callback_query(F.data == "button_lev")
async def send_button_lev(callback: types.CallbackQuery):
    await callback.message.answer(text="Лев — это знак короля, королевы и аристократа. Они гордые существа, рожденные править, рожденные сиять, быть первыми и любящие быть в центре внимания.")
@router.callback_query(F.data == "button_deva")
async def send_button_deva(callback: types.CallbackQuery):
    await callback.message.answer(text="Числа Девы имеют плохую репутацию. Они чрезвычайно преданы и трудолюбивы, с высокими идеалами, большой честностью и любовью к служению.")
@router.callback_query(F.data == "button_vesy")
async def send_button_vesy(callback: types.CallbackQuery):
    await callback.message.answer(text="Управляемые романтической Венерой, Весы являются знаком любви и брака. Их цель — создать гармонию, красоту и спокойствие, поэтому неудивительно, что этот знак ассоциируется с художником, любовником и дипломатом. ")
@router.callback_query(F.data == "button_scorpion")
async def send_button_scorpion(callback: types.CallbackQuery):
    await callback.message.answer(text="Скорпион — знак, характеристика которого для многих непонятна. Собачьи Скорпионы знают, что жизнь незначительна, и в результате живут более страстно.")
@router.callback_query(F.data == "button_strelec")
async def send_button_strelec(callback: types.CallbackQuery):
    await callback.message.answer(text="Стрелец — символ путешественника и философа. Они могут не знать смысла жизни, но они знают, что жизнь имеет смысл, и ищут его.")
@router.callback_query(F.data == "button_kozerog")
async def send_button_kozerog(callback: types.CallbackQuery):
    await callback.message.answer(text="Козероги ассоциируются с ответственностью и властью. Родившийся под серьезным Сатурном, этот знак известен своей энергией, решимостью и сильным трудолюбием.")
@router.callback_query(F.data == "button_vodoley")
async def send_button_vodoley(callback: types.CallbackQuery):
    await callback.message.answer(text="Водолей — знак бунтаря и нонконформиста. Эти личности умны, упрямы, рациональны и эксцентричны.")
@router.callback_query(F.data == "button_ryby")
async def send_button_ryby(callback: types.CallbackQuery):
    await callback.message.answer(text="Управляемые вдохновляющим Нептуном, собачьи Рыбы управляют невидимым и неизученным миром вдохновения и воображения.")