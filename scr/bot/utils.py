from datetime import datetime


def unix_to_timestamp(unix_time: int) -> datetime:
    """Преобразование Unix timestamp в объект datetime для TIMESTAMP в БД."""
    return datetime.fromtimestamp(unix_time)


def get_user_display_name(message) -> str:
    """Получение имени пользователя для записи в базу данных."""
    return message.from_user.username or f"{message.from_user.first_name} {message.from_user.last_name}"