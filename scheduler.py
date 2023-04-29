async def close_queue(inline_message_id, bot, redis_id, client):

    try:
        await bot.edit_message_reply_markup(
            inline_message_id=inline_message_id,
            reply_markup=None
        )
    finally:
        client.delete(redis_id, f'{redis_id}:names')



