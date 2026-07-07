import hashlib
import hmac
from urllib.parse import parse_qsl

from app.core.config import TELEGRAM_BOT_TOKEN


def validate_telegram_data(init_data: str) -> dict:
    data = dict(parse_qsl(init_data))

    received_hash = data.pop("hash")

    secret_key = hmac.new(
        b"WebAppData",
        TELEGRAM_BOT_TOKEN.encode(),
        hashlib.sha256,
    ).digest()

    data_check_string = "\n".join(
        f"{k}={v}" for k, v in sorted(data.items())
    )

    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(calculated_hash, received_hash):
        raise ValueError("Invalid Telegram auth")

    return data