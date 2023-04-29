import os

from aiogram import types

from loader import dp

file_id = 'AgACAgIAAxkDAAMhY_-5NidKEA5rOAaWvGORR-wzJRUAAlXOMRsSI_lLMpQSDDxad9UBAAMCAAN3AAMuBA'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    mes = await message.answer_photo(types.InputFile(path_or_bytesio='IMG_3137.jpg'))
    print(mes.photo[-1].file_id)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    mg = types.MediaGroup()
    mg.attach_photo(file_id)
    mg.attach_photo(file_id)
    mg.attach_photo(file_id)
    await message.answer_media_group(mg)