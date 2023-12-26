from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni yuborish", request_contact=True)
        ]
    ], resize_keyboard=True
)

test_maker = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖New_test")
        ]
    ], resize_keyboard=True
)

select_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕵🏻‍♂️Select_test"),
            KeyboardButton(text="📖About🤵")
        ]
    ], resize_keyboard=True
)

user_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️BACK")
        ]
    ], resize_keyboard=True
)

new_answer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖Again"),
            KeyboardButton(text="🛑The End📖")
        ]
    ], resize_keyboard=True
)


