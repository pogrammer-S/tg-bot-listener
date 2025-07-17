from scr.database.db_service import get_analysis_data
from scr.bot.bot import bot
from scr.config.config import load_config
from scr.llm.client import summarize_dialogue


def run_weekly_pipeline():
    config = load_config()
    # 1. Получить сообщения за нужное время
    data = get_analysis_data()
    # 2. Обработать данные через LLM (заглушка)
    summary = summarize_dialogue(data)
    # 3. Отправить результат в чат
    bot.send_message(config.CHAT_ID, summary)