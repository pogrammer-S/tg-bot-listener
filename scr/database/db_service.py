from scr.database.connection import connection

def save_message(id:int, message:str, date:int):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO messages (user_id , message_text, date_message) VALUES(%s, %s, %s);", (id, message, date))

        #elif message.photo:
        #    cursor.execute("INSERT INTO attachments (user_id , mime_type, paths) VALUES(%s, %s, %s);", (message.from_user.id, bot.get_file(message.photo[-1].file_id).file_path.split(".")[-1], message.photo[-1].file_id))

def new_user(id:int, username:str, date:int):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM users WHERE id = %s", (id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (id , t_name, created_date) VALUES(%s, %s, %s);", (id, username, date))

def test_analysis(bot, person:int):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        bot.send_message(person, str(cursor.fetchall()))

        cursor.execute("SELECT * FROM messages")
        bot.send_message(person, str(cursor.fetchall()))