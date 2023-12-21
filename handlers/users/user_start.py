from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.user import channel_url_keyboard
from data.config import ADMINS
from states.user import RegisterStates, SelectStates
from loader import dp
from aiogram.dispatcher import FSMContext
from utils.checker import check
from utils.db_api.user_commands import get_user, add_user
from keyboards.default.user import phone_number, select_test
from keyboards.default.user import test_maker


@dp.message_handler(CommandStart(), chat_id=ADMINS)
async def bot_start(message: types.Message):
    text = "Assaalomu aleykum Muxriddin aka test yaratish uchun '📖New_test' knopkaga bosing"
    await message.answer(text=text, reply_markup=test_maker)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    checker = await check(user_id=message.chat.id)
    if checker:
        if await get_user(chat_id=message.chat.id):
            text = "Assalomu alaykum, xush kelibsiz."
            await message.answer(text=text, reply_markup=select_test)
        else:
            text = "Assalomu aleykum iltimos ismingizni kiriting"
            await message.answer(text=text)
            await RegisterStates.full_name.set()
    else:
        text = "Kanalga podpiska tasha"
        await message.answer(text=text, reply_markup=channel_url_keyboard)


@dp.message_handler(state=RegisterStates.full_name)
async def f_handler(messege: types.Message, state: FSMContext):
    text = "Telefon raqamingizni kiriting"
    await messege.answer(text=text, reply_markup=phone_number)
    await state.update_data(full_name=messege.text)
    await RegisterStates.phone_number.set()


@dp.message_handler(state=RegisterStates.phone_number, content_types=types.ContentType.CONTACT)
async def phone_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number, chat_id=message.chat.id, created_at=message.date)
    data = await state.get_data()
    user = await add_user(data=data)
    if user:
        text = "Test botimizga xush kelibsiz. Siz muvafaqqiyatli ro'yxatdan o'tdingiz."
    else:
        text = "Bot has some problem"
    await message.answer(text=text, reply_markup=select_test)
    await state.finish()

@dp.message_handler(text = "🕵🏻‍♂️Select_test")
async def select_test_handler(message:types.Message):
    text = "Iltimos tekshirmoqchi bolgan test tingizni codini kiriting"
    await message.answer(text=text)
    await SelectStates.set()

