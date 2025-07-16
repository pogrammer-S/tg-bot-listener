from scr.bot.bot import bot
from scr.scheduler.scheduler import start_scheduler
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    start_scheduler()
    bot.polling(none_stop=True)
