from .bot import bot, markup
from scr.scheduler.pipline import run_weekly_pipeline
from scr.scheduler.scheduler import scheduler, start_scheduler
from datetime import datetime
from scr.config.config import load_config

@bot.message_handler(commands=['start'])
def command_start(message):
    config = load_config()
    start_scheduler(datetime.now().strftime('%a').lower(), datetime.now().hour)
    bot.send_message(config.CHAT_ID, f"Проверка запущенна в {datetime.now().strftime('%a').lower()}, {datetime.now().hour}")

@bot.message_handler(commands=['stop'])
def command_stop(message):
    config = load_config()
    scheduler.remove_all_jobs()
    bot.send_message(config.CHAT_ID, "Проверка остановленна")

@bot.message_handler(commands=['return'])
def command_return(message):
    run_weekly_pipeline()

@bot.message_handler(commands=['help'])
def command_help(message):
    config = load_config()
    bot.send_message(config.CHAT_ID, """
    Доступные команды:
    /start - Запуск еженедельных проверок от текущего момента(Удаляет все остальные проверки)
    /stop - Удаление проверки
    /return - Возращение ответа LMM игнорируя проверку
    /help - Список команд
""", reply_markup=markup)