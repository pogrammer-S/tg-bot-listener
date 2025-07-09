import telebot
import psycopg2

bot = telebot.TeleBot("7772980080:AAGwUXoFhXXAaIJZtzp2XGSNm2B3hoUIXZU")
connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "322692",
        database = "postgres"
    )
connection.autocommit = True

with open("init.sql", "r") as script:
    with connection.cursor() as cursor:
        cursor.execute(script.read())


@bot.message_handler(func=lambda message: True)
def new_message(message):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO messages (username , message_user, date_message) VALUES(%s, %s, %s)" % (str(message.from_user.username), str(message.text), str(message.date)))

bot.polling()
connection.close()