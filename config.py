import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
redis_ip = os.getenv('REDIS_IP')
time_zone = os.getenv('TIME_ZONE')