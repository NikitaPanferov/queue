import uuid

from aiogram import types

from loader import dp
from markups import get_button, get_manual_buttons


@dp.inline_handler()
async def start_queue(query: types.InlineQuery):
    if query.query:
        articles = [types.InlineQueryResultArticle(
            id=uuid.uuid4().hex,
            title='Голосование с автоматическим завершением',
            description=query.query,
            input_message_content=types.InputMessageContent(message_text=query.query),
            reply_markup=await get_button(query.query)
        ),
        types.InlineQueryResultArticle(
            id=uuid.uuid4().hex,
            title='Голосование с ручным завершением',
            description=query.query,
            input_message_content=types.InputMessageContent(message_text=query.query),
            reply_markup=await get_manual_buttons(query.query, query.from_user.id)
        ),
        ]
    else:
        articles = [types.InlineQueryResultArticle(
            id=uuid.uuid4().hex,
            title='Введите тему для очереди',
            input_message_content = types.InputMessageContent(message_text='Бот для создания очереди')
        )]

    await query.answer(articles, cache_time=1, is_personal=True)
