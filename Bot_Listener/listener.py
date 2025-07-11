from SQL_Con.ConnectionSQL import connection
from Bot_Listener.Bot import bot

@bot.message_handler(content_types=['text'])
def new_message(message):
    print()
    with connection.cursor() as cursor:
        if message.text:
            cursor.execute("INSERT INTO messages (user_id , message_user, date_message) VALUES(%s, %s, %s);", (message.from_user.id, message.text, message.date))
        #elif message.photo:
        #    cursor.execute("INSERT INTO attachments (user_id , mime_type, paths) VALUES(%s, %s, %s);", (message.from_user.id, bot.get_file(message.photo[-1].file_id).file_path.split(".")[-1], message.photo[-1].file_id))
        
        cursor.execute("SELECT 1 FROM users WHERE t_id = %s", (message.from_user.id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (t_id , t_name, created_date) VALUES(%s, %s, %s);", (message.from_user.id, message.from_user.username, message.date))
        
        bot.reply_to(message, "Полученно")