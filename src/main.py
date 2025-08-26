import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config import settings
from src.api.include_routers import all_routers

dp = Dispatcher()


def include_routers(dp: Dispatcher, routers: tuple) -> None:
    for router in routers:
        dp.include_router(router)


async def main(routers: tuple) -> None:
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    include_routers(dp, routers)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(all_routers))
