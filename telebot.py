import asyncio
from dotenv import load_dotenv
import os
import openai
import sys
from aiogram import Bot, types, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart


load_dotenv()  # This is done to access the .env file
openai.api_key = os.getenv("OPENAI_API_KEY") # This is done to access OPENAI key
BOT_TOKEN = os.getenv('TOKEN') # This is done to access BOT key

# model_name
MODEL_NAME = 'gpt-3.5-turbo'

# Initialize Bot instance with a default parse mode which will be passed to all API calls    
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)  # Setting the bot object

# This helps us to connect with the telegram bot
dp = Dispatcher() 

async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)

# This class will be used to store the previous response given by bot
class Reference():
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

# A function to clear the previous conversation and context.
def clear_past():
    reference.response = ""

# This handler receives messages with `/start` or  `/help `command
@dp.message(CommandStart())
async def welcome(message:types.Message):
    await message.reply('Hi\n I am a tele bot\n Powered by Shiva. How can i assist you?')

# A handler to clear the previous conversation and context.
@dp.message(CommandStart())
async def clear(message:types.Message):
    await message.reply("I've cleared the past conversation and context.")

# A handler to display the help menu.  
@dp.message(CommandStart())
async def helper(message:types.Message):
    
    help_command = """
    Hi There, I'm chatGPT Telegram bot created by Bappy! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :) """
    
    await message.reply("help_command")

# A handler to process the user's input and generate a response using the chatGPT API.
@dp.message()
async def chatgpt(message:types.Message):
    print(f">>> USER: \n\t{message.text}")
    response = openai.Completion.create(
        model = MODEL_NAME,
        message = [
            {'role' : 'assistant', 'content' : reference.response}, # Role assistant 
            {'role' : 'user', 'content' : message.text} # Our Query 
        ]
    )
    reference.response = response['choice'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id= message.chat.id, text = reference.response)
    
if __name__ == '__main__':
    asyncio.run(main())

