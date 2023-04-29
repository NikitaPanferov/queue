import logging
from loader import scheduler


async def on_start(dp):
    scheduler.start()

if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    logging.basicConfig(level=logging.INFO)

    executor.start_polling(dp, skip_updates=True, on_startup=on_start)