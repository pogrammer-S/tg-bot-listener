from apscheduler.schedulers.background import BackgroundScheduler
from scr.bot.bot import return_analysis_in_chat

scheduler = BackgroundScheduler()
scheduler.add_job(return_analysis_in_chat, 'cron', day_of_week='mon', hour=9)
scheduler.start()