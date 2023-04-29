from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_button(title):
    return InlineKeyboardMarkup(1,[
        [
            InlineKeyboardButton('Занять место', callback_data=f'title')
        ]
    ])


async def get_manual_buttons(title, owner):
    return InlineKeyboardMarkup(2, [
        [
            InlineKeyboardButton('Занять место', callback_data=f'/::manual {owner}:-:-:{title}'),
            InlineKeyboardButton('Завершить голосование', callback_data=f'finish:-:-:{owner}')
        ]
    ])
