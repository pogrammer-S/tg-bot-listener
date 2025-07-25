from scr.bot.bot import bot
from scr.scheduler.scheduler import start_scheduler, scheduler
import logging
from datetime import datetime

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    start_scheduler(datetime.now().strftime('%a').lower(), datetime.now().hour)
    scheduler.start()
    bot.polling(none_stop=True)
