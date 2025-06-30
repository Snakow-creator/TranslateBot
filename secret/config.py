from dotenv import load_dotenv
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_PROPERTIES = DefaultBotProperties(parse_mode=ParseMode.HTML)
