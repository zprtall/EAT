from datetime import datetime

from app.tasks.reminders import check_user_habits
from app.models.user import User
from app.models.meal import Meal



def create_user(db, telegram_id=123, habits=None):
    user = User(
        telegram_id=telegram_id,
        habit_times=habits or []
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_meal(db, user_id, dt):
    meal = Meal(
        user_id=user_id,
        created_at=dt
    )
    db.add(meal)
    db.commit()
    return meal


def test_send_reminder_when_no_meal(monkeypatch, db_session):
    called = {"value": False}

    def fake_send(chat_id):
        called["value"] = True

    monkeypatch.setattr(
        "app.tasks.habit_tasks.send_telegram_reminder",
        fake_send
    )

    now = datetime.utcnow()

    user = create_user(
        db_session,
        habits=[now.strftime("%H:%M")]
    )

    check_user_habits()

    assert called["value"] is True


# 🔥 2. НЕ должен отправить, если уже ел сегодня
def test_no_reminder_if_user_ate(monkeypatch, db_session):
    called = {"value": False}

    def fake_send(chat_id):
        called["value"] = True

    monkeypatch.setattr(
        "app.tasks.habit_tasks.send_telegram_reminder",
        fake_send
    )

    now = datetime.utcnow()

    user = create_user(
        db_session,
        habits=[now.strftime("%H:%M")]
    )

    create_meal(db_session, user.id, now)

    check_user_habits()

    assert called["value"] is False


# 🔥 3. НЕ должен отправить, если время не совпадает
def test_no_reminder_if_time_not_match(monkeypatch, db_session):
    called = {"value": False}

    def fake_send(chat_id):
        called["value"] = True

    monkeypatch.setattr(
        "app.tasks.habit_tasks.send_telegram_reminder",
        fake_send
    )

    now = datetime.utcnow()

    user = create_user(
        db_session,
        habits=["23:59"]  # почти никогда не совпадёт
    )

    check_user_habits()

    assert called["value"] is False


def test_habit_calculation(db_session):
    from app.services.analytics_service import get_user_habit_times

    base = datetime.utcnow().replace(minute=10, second=0, microsecond=0)

    meals = [
        Meal(created_at=base.replace(hour=9)),
        Meal(created_at=base.replace(hour=9)),
        Meal(created_at=base.replace(hour=14)),
        Meal(created_at=base.replace(hour=14)),
        Meal(created_at=base.replace(hour=20)),
    ]

    habits = get_user_habit_times(meals)

    assert len(habits) == 3


def test_no_spam(monkeypatch, db_session):
    called = {"count": 0}

    def fake_send(chat_id):
        called["count"] += 1

    monkeypatch.setattr(
        "app.tasks.habit_tasks.send_telegram_reminder",
        fake_send
    )

    now = datetime.utcnow()

    user = create_user(
        db_session,
        habits=[now.strftime("%H:%M")]
    )

    user.last_reminder_at = now
    db_session.commit()

    check_user_habits()

    assert called["count"] == 0