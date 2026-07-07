from sqladmin import ModelView
from app.models.user import User

class Users(ModelView, model=User):
    column_list = [
        User.id,
        User.telegram_id,
        User.last_reminder_at
    ]