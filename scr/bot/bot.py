import telebot
import os
from dotenv import load_dotenv
from scr.scheduler.pipline import returm_analysis_lmm

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def return_analysis_in_chat():
    bot.send_message(os.getenv("Test_chat"), returm_analysis_lmm())