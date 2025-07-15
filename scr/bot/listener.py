from scr.database.db_service import save_message, new_user
from scr.bot.bot import bot

@bot.message_handler(content_types=['text'])
def new_message(message):
    if not message.text:
        return
    
    new_user(message.from_user.id, message.from_user.username, message.date)
    save_message(message.from_user.id, message.text, message.date)
    

    bot.reply_to(message, "Полученно")