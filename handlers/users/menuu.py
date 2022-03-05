from cgitb import text
from loader import dp
from aiogram import types
from keyboards.inline.katalog import katalog
from aiogram.dispatcher import FSMContext
from states.st import anketa


@dp.callback_query_handler(text="shashlik")
async def katalog(message: types.Message):
    await message.answer_photo("C:\Users\iskan\OneDrive\Изображения\Пленка\photo_2022-03-03_18-35-51.jpg")
    await message.answer(text="Кусковой \n\n Говядина")

@dp.callback_query_handler(text="bludo2")
async def katalog2(message: types.Message):
    await message.answer_photo("C:\Users\iskan\OneDrive\Изображения\Пленка\photo_2022-03-03_18-40-31.jpg")
    await message.answer(text="Мясо по-царски \n \nСвинина по царски в духовке. Вкусное и сытное мясное блюдо для праздника! Такое блюдо отличается отменным, богатым вкусом и неповторимым ароматом.")

@dp.callback_query_handler(text="frozen")
async def katalog3(message: types.Message):
    await message.answer_photo("C:\Users\iskan\OneDrive\Изображения\Пленка\photo_2022-03-03_18-43-26.jpg")
    await message.answer(text="Свежие нарезки \n\nНарезки на звонок - Скачать бесплатно на телефон, музыкальные обрезки на рингтон мобильного, нарезки современной музыки для звонка, вырезки и отрывки на")

