import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config import settings
from src.api.include_handlers import all_handlers

dp = Dispatcher()


def include_handlers(dp: Dispatcher, routers: tuple):
    for router in routers:
        dp.include_router(router)


async def main(handlers: tuple) -> None:
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    include_handlers(dp, handlers)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(all_handlers))
