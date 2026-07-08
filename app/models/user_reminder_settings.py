from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Integer, ForeignKey


class UserReminderSettings(Base):

    __tablename__ = "user_reminder_settings"


    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),unique=True)
    reminders_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    user = relationship("User", back_populates="reminder_settings")
