import telebot
import os
from dotenv import load_dotenv
from scr.database.db_service import test_analysis

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def Analysis():
    test_analysis(bot, os.getenv("Test_chat"))