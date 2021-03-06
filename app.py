from aiogram import executor
from utils.notify_admins import on_startup_notify
from handlers.users import *


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
