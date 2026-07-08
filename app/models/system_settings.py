from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer


class SystemSettings(Base):
    __tablename__ = "system_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    reminders_enabled: Mapped[bool] = mapped_column(Boolean, default=True)