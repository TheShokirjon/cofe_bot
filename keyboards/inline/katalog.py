from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

katalog = InlineKeyboardButton[
    [
        InlineKeyboardButton("Шашлык", callback_data="shashlik"),
        InlineKeyboardButton("Второе блюдо", callback_data="bludo2"),
        InlineKeyboardButton("Холодные Закуски", callback_data="frozen"),
    ]
]