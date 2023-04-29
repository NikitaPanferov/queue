from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import redis
import config

client = redis.Redis(config.redis_ip, charset="utf-8", decode_responses=True)
scheduler = AsyncIOScheduler(timezone=config.time_zone, job_defaults={'misfire_grace_time': 600})
bot = Bot(config.token)
dp = Dispatcher(bot)
