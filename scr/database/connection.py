from scr.config.config import load_config
import psycopg2
from psycopg2 import pool

config = load_config()

POSTGRES_PARAMS = {
    'host': config.DB_HOST,
    'user': config.DB_USER,
    'password': config.DB_PASSWORD,
    'database': config.DB_NAME,
    'port': config.DB_PORT
}

connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, **POSTGRES_PARAMS)


def get_connection():
    return connection_pool.getconn()


def put_connection(conn):
    connection_pool.putconn(conn)
