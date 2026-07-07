from app.models.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, BigInteger, JSON, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    habit_times: Mapped[list] = mapped_column(JSON, default=list)
    last_reminder_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    body_params = relationship("BodyParam", back_populates="user")
    dishes = relationship("Dish", back_populates="user")
    meals = relationship("Meal", back_populates="user")
    nutrition_target = relationship("NutritionTarget", back_populates="user", uselist=False)