from scr.database.connection import connection

def store_message(id:int, message:str, date:int):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO messages (user_id , message_text, created_at) VALUES(%s, %s, %s);", (id, message, date))

        #elif message.photo:
        #    cursor.execute("INSERT INTO attachments (user_id , mime_type, paths) VALUES(%s, %s, %s);", (message.from_user.id, bot.get_file(message.photo[-1].file_id).file_path.split(".")[-1], message.photo[-1].file_id))

def store_user(id:int, t_name:str, date:int):
    with connection.cursor() as cursor:
        t_name = t_name if t_name != None else "No_username"
        if not is_user_exist(id):
            cursor.execute("INSERT INTO users (id , t_name, created_at) VALUES(%s, %s, %s);", (id, t_name, date))

def get_analysis_data():
    with connection.cursor() as cursor:
        itog = []
        cursor.execute("SELECT * FROM users")
        itog += str(cursor.fetchall())

        cursor.execute("SELECT * FROM messages")
        itog += str(cursor.fetchall())

        return itog

def is_user_exist(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM users WHERE id = %s", (id,))
        return cursor.fetchone()