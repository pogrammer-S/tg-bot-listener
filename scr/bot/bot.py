import telebot
from scr.config.config import load_config

config = load_config()
bot = telebot.TeleBot(config.TOKEN)