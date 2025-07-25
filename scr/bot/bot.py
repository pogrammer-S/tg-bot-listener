import telebot
from scr.config.config import load_config
from telebot import types

config = load_config()
bot = telebot.TeleBot(config.TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
button_start = types.KeyboardButton("/start")
button_stop = types.KeyboardButton("/stop")
button_return = types.KeyboardButton("/return")
button_help = types.KeyboardButton("/help")

markup.add(button_start, button_stop, button_return, button_help)