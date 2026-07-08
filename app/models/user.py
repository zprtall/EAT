from app.models.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, BigInteger, JSON, DateTime, String
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)

    habit_times: Mapped[list] = mapped_column(JSON, default=list)
    last_reminder_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    reminder_settings = relationship("UserReminderSettings", back_populates="user", uselist=False,
                                     cascade="all, delete-orphan")

    body_params = relationship("BodyParam", back_populates="user")
    dishes = relationship("Dish", back_populates="user")
    meals = relationship("Meal", back_populates="user")
    nutrition_daily_target = relationship("NutritionDailyTarget", back_populates="user", uselist=False)
