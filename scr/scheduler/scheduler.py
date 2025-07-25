from apscheduler.schedulers.background import BackgroundScheduler
from scr.scheduler.pipline import run_weekly_pipeline

scheduler = BackgroundScheduler()

def start_scheduler(current_day, current_hour):
    scheduler.remove_all_jobs()
    scheduler.add_job(run_weekly_pipeline, 'cron', day_of_week=current_day, hour=current_hour)
    return scheduler