from app.core.celery import celery
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.meal import Meal
from app.models.user import User
from app.models.system_settings import SystemSettings
from app.services.analytics_service import get_user_habit_times
from app.services.telegram_service import send_telegram_reminder


@celery.task
def check_user_habits():
    session: Session = SessionLocal()
    users = session.query(User).all()
    system_settings = session.query(
        SystemSettings
    ).first()

    if not system_settings:
        session.close()
        return

    if not system_settings.reminders_enabled:
        session.close()
        return

    now = datetime.now(timezone.utc)

    for user in users:
        if user.reminder_settings:
            if not user.reminder_settings.reminders_enabled:
                continue
        meals = session.query(Meal).filter(
            Meal.user_id == user.id,
            Meal.created_at >= now - timedelta(days=30)
        ).all()
        habit_times = get_user_habit_times(meals)
        if not habit_times:
            continue
        today_start = datetime(
            now.year,
            now.month,
            now.day
        )
        today_meal = session.query(Meal).filter(
            Meal.user_id == user.id,
            Meal.created_at >= today_start
        ).first()
        if today_meal:
            continue
        for habit_time in habit_times:
            if abs(
                (now - habit_time).total_seconds()
            ) <= 1800:
                if (
                    user.last_reminder_at
                    and
                    (now - user.last_reminder_at).seconds < 3600
                ):
                    continue
                send_telegram_reminder(
                    user.telegram_id
                )
                user.last_reminder_at = now
                session.commit()
                break
    session.close()
