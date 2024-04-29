import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

TOKEN = '6806758618:AAGfqwxt2eBWYyKkJktkwOTONWv-M-UtbWg'

bot = Bot(TOKEN)
dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    from handlers import dp

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

    """
    #   название                Menu_id     parrent_id
    1 - Бакалавриат             меню1       0
    2 - Магистратура            меню1       0

    3 - Информатика             меню2       меню1
    4 - Безопасность            меню2       меню1

    5 - Информатика             меню3       меню1
    6 - Безопастность           меню3       меню1

    7 - Общая инфа              меню4       меню3
    8 - Условия поступления     меню4       меню3

    9 - Общая инфа              меню5       меню3
    10 - Условия поступления    меню5       меню3
    """
