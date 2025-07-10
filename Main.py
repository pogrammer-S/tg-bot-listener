import telebot
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

connection = psycopg2.connect(
        host = "postgres",
        user = "postgres",
        password = "postgres",
        database = "postgres",
        port = 5432
)
connection.autocommit = True

with open("init.sql", "r") as script:
    with connection.cursor() as cursor:
        cursor.execute(script.read())


@bot.message_handler(func=lambda message: True)
def new_message(message):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO messages (username , message_user, date_message) VALUES(%s, %s, %s);", (message.from_user.username, message.text, message.date))
        bot.reply_to(message, "Записанно")

bot.polling()
connection.close()