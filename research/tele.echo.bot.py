import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os
import asyncio
from os import getenv
import sys
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

load_dotenv()  # This is done to access the .env file
BOT_TOKEN = os.getenv('TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Bot instance with a default parse mode which will be passed to all API calls    
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)  # Setting the bot object

# This helps us to connect with the telegram bot
dp = Dispatcher() 

async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)

# Below is created to start communication with bot
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help `command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


@dp.message()
async def echo_handler(message: types.Message):
    """
    This will retrun echo
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

if __name__ == "__main__":
    asyncio.run(main())
