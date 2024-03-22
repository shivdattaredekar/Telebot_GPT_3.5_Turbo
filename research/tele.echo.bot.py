import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os
import asyncio
from os import getenv
import sys


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
@dp.message(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help `command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())