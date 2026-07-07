import requests
from app.core.config import TELEGRAM_BOT_TOKEN

def send_telegram_reminder(telegram_id: int):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={
            "chat_id": telegram_id,
            "text": "Пора внести калории!"
        }
    )