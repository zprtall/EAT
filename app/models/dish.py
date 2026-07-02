from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey

class Dish(Base):
    __tablename__ = "dishes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    weight_finish_dish: Mapped[float] = mapped_column(Float, nullable=True)
    is_finished: Mapped[bool] = mapped_column(default=False)
    calories: Mapped[float | None] = mapped_column(Float, nullable=True)
    proteins: Mapped[float | None] = mapped_column(Float, nullable=True)
    fats: Mapped[float | None] = mapped_column(Float, nullable=True)
    carbs: Mapped[float | None] = mapped_column(Float, nullable=True)

    user = relationship("User", back_populates="dishes")
    ingredients = relationship(
        "Ingredient",
        back_populates="dish",
        cascade="all, delete-orphan"
    )
    meal_items = relationship("MealItem", back_populates="dish")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index = True)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id"), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    proteins: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)

    dish = relationship("Dish", back_populates="ingredients")