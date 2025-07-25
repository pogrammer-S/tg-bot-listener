import requests
from scr.config.config import load_config
import json

config = load_config()
webhook_url = config.WEBHOOK_URL

def summarize_dialogue(data):
    # Отправака и получение ответа от LLM
    if not data:
        return "Нет сообщений для анализа."
    
    try:
        response = requests.post(webhook_url, json=json.dumps(data))
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return "Ошибка при запросе к LLM:" + str(e)