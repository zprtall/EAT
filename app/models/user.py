from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body_params = relationship("BodyParam", back_populates="user")
    dishes = relationship("Dish", back_populates="user")
    meals = relationship("Meal", back_populates="user")
    nutrition_target = relationship("NutritionTarget", back_populates="user", uselist=False)
