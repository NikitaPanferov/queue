from loader import dp, client, bot, scheduler
from aiogram import types
from scheduler import close_queue
from markups import get_button, get_manual_buttons
from datetime import datetime, timedelta


manual_regexp = r'^/::manual .*$'
finish_regexp = r'^finish:-:-:.*$'


@dp.callback_query_handler(regexp=finish_regexp)
async def finish(call: types.CallbackQuery):
    if call.from_user.id == int(call.data.split(':-:-:')[1]):
        await close_queue(inline_message_id=call.inline_message_id, bot=bot, redis_id=call.inline_message_id, client=client)
        await call.answer()
    else:
        await call.answer('Вы не создатель голосования')


@dp.callback_query_handler(regexp=manual_regexp)
async def manual_voice(call:types.CallbackQuery):
    splited = call.data.split(':-:-:')
    id = call.inline_message_id
    owner = splited[0].split()[1]
    title = splited[1]

    # if str(call.from_user.id) in client.lrange(id, 0, -1):
    #     await call.answer('Уже в очереди')
    #     return

    client.rpush(id, call.from_user.id)
    client.rpush(f'{id}:names', call.from_user.full_name)
    text = '\n'.join([f'{idx+1}. {name}' for idx, name in enumerate(client.lrange(f'{id}:names', 0, -1))])

    await bot.edit_message_text(
        text=f'{title}\n{text}',
        inline_message_id=call.inline_message_id,
        reply_markup=await get_manual_buttons(title, owner)
    )




@dp.callback_query_handler()
async def set_user(call: types.CallbackQuery):
    # id = call.data.split(':-:-:')[0]
    # title = call.data.split(':-:-:')[1]
    title = call.data
    id = call.inline_message_id

    if not client.lrange(id, 0, -1):
        scheduler.add_job(close_queue, trigger='date', run_date=datetime.now() + timedelta(days=1), kwargs=dict(
            inline_message_id=call.inline_message_id, bot=bot, redis_id=id, client=client))

    if str(call.from_user.id) in client.lrange(id, 0, -1):
        await call.answer('Уже в очереди')
        return

    client.rpush(id, call.from_user.id)
    client.rpush(f'{id}:names', call.from_user.full_name)
    text = '\n'.join([f'{idx+1}. {name}' for idx, name in enumerate(client.lrange(f'{id}:names', 0, -1))])

    await bot.edit_message_text(
        text=f'{title}\n{text}',
        inline_message_id=call.inline_message_id,
        reply_markup=await get_button(title)
    )

    await call.answer()


