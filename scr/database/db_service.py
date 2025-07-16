from contextlib import contextmanager
import logging
from datetime import datetime
from typing import Any, Optional, List, Tuple, Literal
from scr.database.connection import get_connection, put_connection


@contextmanager
def db_connection():
    """Контекстный менеджер для соединения с базой данных."""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        logging.error(f"Ошибка базы данных: {e}")
        conn.rollback()
        raise
    finally:
        put_connection(conn)


def execute_query(query: str, params: tuple = (), fetch: Optional[Literal["one", "all"]] = None) -> Optional[Any]:
    """Универсальная функция для выполнения SQL-запросов с автосозданием соединения."""
    with db_connection() as conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch == "one":
                    return cursor.fetchone()
                if fetch == "all":
                    return cursor.fetchall()
        except Exception as e:
            logging.error(f"Ошибка выполнения запроса: {e}")
            raise


def store_message(id: int, message: str, date: Optional[datetime] = None) -> Optional[int]:
    """Сохранение сообщения в базу данных."""
    date = date or datetime.now()
    query = "INSERT INTO messages (user_id, text, created_at) VALUES (%s, %s, %s) RETURNING id;"
    result = execute_query(query, (id, message, date), fetch="one")
    return result[0] if result else None


def store_user(id: int, t_name: str, date: Optional[datetime] = None) -> None:
    """Сохранение нового пользователя."""
    date = date or datetime.now()
    t_name = t_name or "No_username"
    query = "INSERT INTO users (id, t_name, created_at, updated_at) VALUES (%s, %s, %s, %s);"
    execute_query(query, (id, t_name, date, date))


def update_user(id: int, t_name: str, updated_at: Optional[datetime] = None) -> None:
    """Обновление данных пользователя."""
    updated_at = updated_at or datetime.now()
    query = "UPDATE users SET t_name = %s, updated_at = %s WHERE id = %s;"
    execute_query(query, (t_name, updated_at, id))


def store_attachment(message_id: int, mime_type: str, path: str) -> None:
    """Сохранение вложения."""
    query = "INSERT INTO attachments (message_id, mime_type, path) VALUES (%s, %s, %s);"
    execute_query(query, (message_id, mime_type, path))


def get_analysis_data() -> List[Tuple]:
    """Получение данных для анализа."""
    query = '''
        SELECT u.id, u.t_name, u.created_at AS user_created_at, m.text, m.created_at AS message_created_at
        FROM messages m
        JOIN users u ON m.user_id = u.id
        ORDER BY m.created_at
    '''
    return execute_query(query, fetch="all") or []


def get_user_name_by_id(id: int) -> Optional[str]:
    """Получение имени пользователя по ID."""
    query = "SELECT t_name FROM users WHERE id = %s;"
    result = execute_query(query, (id,), fetch="one")
    return result[0] if result else None


def upsert_user(id: int, t_name: str) -> None:
    """Обновление или вставка пользователя."""
    current_name = get_user_name_by_id(id)
    if current_name is None:
        store_user(id, t_name)
    elif current_name != t_name:
        update_user(id, t_name)
