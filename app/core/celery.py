from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)


celery.conf.beat_schedule = {
    "check-habits": {
        "task": "app.tasks.reminders.check_user_habits",
        "schedule": crontab(minute=0),
    },
}

celery.conf.timezone = "UTC"