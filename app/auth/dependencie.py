import json
from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.auth.telegram_auth import validate_telegram_data
from app.repositories.user_repo import UserRepo
from app.models.user import User
from app.core.config import settings

def get_current_user(
    session: Session = Depends(get_session),
    x_telegram_auth: str = Header(None)
):
    if settings.DEBUG:
        telegram_id = 123456789

        repo = UserRepo()
        user = repo.get_by_telegram_id(session, telegram_id)

        if not user:
            user = User(
                telegram_id=telegram_id,
                username="dev_user",
                first_name="Dev"
            )
            user = repo.create(session, user)

        return user

    if not x_telegram_auth:
        raise HTTPException(status_code=401, detail="No Telegram auth header")

    try:
        data = validate_telegram_data(x_telegram_auth)

        user_data = json.loads(data["user"])
        telegram_id = user_data["id"]

        repo = UserRepo()
        user = repo.get_by_telegram_id(session, telegram_id)

        if not user:
            user = User(
                telegram_id=telegram_id,
                username=user_data.get("username"),
                first_name=user_data.get("first_name"),
            )
            user = repo.create(session, user)

        return user

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))