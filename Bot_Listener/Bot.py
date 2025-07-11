import telebot
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from SQL_Con.ConnectionSQL import connection

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

def Analysis():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        bot.send_message(719467479, str(cursor.fetchall()))

        cursor.execute("SELECT * FROM messages")
        bot.send_message(719467479, str(cursor.fetchall()))


scheduler = BackgroundScheduler()
scheduler.add_job(Analysis, 'cron', day_of_week='mon', hour=9)
scheduler.start()