import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from db import *

TOKEN = "6856878466:AAHsi-iIInEqNeh8gTtyS8XzHzdAoWQywag"#getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!\nНапиши свое желание в следующем сообщении")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        if message.text == "/go":
            efef = distributePlayers()
            for i in efef:
                await bot.send_message(chat_id=i[1], text="ШУТКА")
                textD = f"Ти будеш Тайним Сантою для: {i[2][0]}, бажання: {i[2][2]}"
                await bot.send_message(chat_id=i[1], text=textD)
        else:
            mwss = add_player(message.from_user.full_name, message.chat.id, message.text)
            if mwss == "new":
                mess = get_info()
                for i in mess:
                    await bot.send_message(chat_id=i[1], text=f"Новий гравець {hbold(message.from_user.full_name)}, тепер нас {len(mess)}")
            await bot.send_message(chat_id=message.chat.id, text=f"Твоє бажання: {message.text}, напиши нове якщо хочеш змінити.")
    except TypeError:
        await message.answer("Error!")


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())