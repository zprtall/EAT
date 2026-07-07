from app.models.user import User

class UserRepo:

    def get_by_telegram_id(self, session, telegram_id: int):
        return session.query(User).filter_by(telegram_id=telegram_id).first()

    def create(self, session, user: User):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user