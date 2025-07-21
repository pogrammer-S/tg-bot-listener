from scr.bot.utils import unix_to_timestamp, get_user_display_name
from scr.database.db_service import store_message, upsert_user, get_analysis_data
from scr.bot.bot import bot


print("handlers запущен")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(719467479, "Обработчик работает...")
    """Обработчик новых сообщений (текст, фото, документы)."""
    try:
        # Обновляем или создаем пользователя
        t_name = get_user_display_name(message)
        upsert_user(message.from_user.id, t_name)

        message_id = store_message(message.from_user.id, message.text, unix_to_timestamp(message.date))

        # TODO: добавить обработчик для attachments (для этого пригодится message_id)

        bot.reply_to(message, "Получено")

    except Exception as e:
        # Для отладки
        bot.reply_to(message, f"Произошла ошибка при обработке сообщения, {str(e)}")

# TODO: добавить ещё хэндлеры

def test_message():
    bot.send_message(719467479, get_analysis_data())