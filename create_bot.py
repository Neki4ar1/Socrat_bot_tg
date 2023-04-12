from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os


bot = Bot(token=os.getenv('TG_HOMETASK_TOKEN', 'Not_Found'))
dp = Dispatcher(bot)
