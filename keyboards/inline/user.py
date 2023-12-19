from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

contact_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Adminga habar yuborish", callback_data="send_message_to_admin")
        ]
    ]
)

user_product_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bozordan olib tashlash", callback_data="delete_from_market"),
            InlineKeyboardButton(text="O'chirib tashlash", callback_data="delete_from_market"),
        ]
    ]
)

channel_url_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanal ga otish", url="https://t.me/otash_live"),
            InlineKeyboardButton(text="✅Check", callback_data="start")
        ]
    ]
)
