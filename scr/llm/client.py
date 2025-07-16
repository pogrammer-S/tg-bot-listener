def summarize_dialogue(data):
    # Заглушка: потом это будет делать LLM
    if not data:
        return "Нет сообщений для анализа."
    users = set(row[1] for row in data)
    return f"За неделю {len(data)} сообщений от {len(users)} пользователей. (Заглушка LLM)"
