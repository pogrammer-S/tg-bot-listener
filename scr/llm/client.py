import requests
from scr.config.config import load_config
from scr.bot.handlers import test_message
import json

config = load_config()
webhook_url = config.WEBHOOK_URL

def summarize_dialogue(data):
    # Заглушка: потом это будет делать LLM
    if not data:
        return "Нет сообщений для анализа."
    
    try:
        test_message()
        response = requests.post(webhook_url, json=json.dumps(data))
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return "Ошибка при запросе к LLM:" + str(e)

    #users = set(row[1] for row in data)
    #return f"За неделю {len(data)} сообщений от {len(users)} пользователей. (Заглушка LLM)"