from apscheduler.schedulers.background import BackgroundScheduler
from scr.scheduler.pipline import run_weekly_pipeline

def start_scheduler():
    scheduler = BackgroundScheduler()
    #scheduler.add_job(run_weekly_pipeline, 'cron', day_of_week='mon', hour=9)
    scheduler.add_job(run_weekly_pipeline, "interval", seconds=30)
    scheduler.start()
    return scheduler