import asyncio

from aiogram import Bot, Dispatcher
from apps import handlers, callbacks
from secret.config import TOKEN, BOT_PROPERTIES
from middlewares.check_subscribe import CheckSubscribtion

bot = Bot(token=TOKEN, default=BOT_PROPERTIES)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers.router, callbacks.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("rasle going to sleep.")
