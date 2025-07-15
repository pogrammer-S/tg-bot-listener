from apscheduler.schedulers.background import BackgroundScheduler
from scr.bot.bot import Analysis

scheduler = BackgroundScheduler()
scheduler.add_job(Analysis, 'cron', day_of_week='mon', hour=9)
scheduler.start()