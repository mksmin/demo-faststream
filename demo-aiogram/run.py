import asyncio
import logging

from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from app.config.config import settings
from app.broker_handlers import broker

router = Router()
log = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello, World!")


async def get_bot() -> Bot:
    bot_instance = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    return bot_instance


async def start_bot():
    settings.log.configurate_logging()
    bot = await get_bot()

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        log.info("Начинаю пуллить бота")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


async def main():
    await asyncio.gather(
        broker.start(),
        start_bot(),
    )


if __name__ == "__main__":
    asyncio.run(main())
