from app.models.models import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
<<<<<<< HEAD
from sqlalchemy import Integer, String, Float, Date, Time, ForeignKey, DateTime
=======
from sqlalchemy import Integer, String, Float, Date, Time, ForeignKey
>>>>>>> dbd197587f071c39fc093ab72511cd8be9e20876
import datetime

class Meal(Base):
    __tablename__ = "meals"

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.utcnow)
    meal_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.utcnow)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    time: Mapped[datetime.time] = mapped_column(Time, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    type: Mapped[str] = mapped_column(String, nullable=False)
    user = relationship("User", back_populates="meals")
    items = relationship(
        "MealItem",
        back_populates="meal",
        cascade="all, delete-orphan"
    )


class MealItem(Base):
    __tablename__ = "meal_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    meal_id: Mapped[int] = mapped_column(ForeignKey("meals.id"))
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id"))
    dish_id: Mapped[int | None] = mapped_column(ForeignKey("dishes.id"))
    grams: Mapped[float] = mapped_column(Float, nullable=False)

    meal = relationship("Meal", back_populates="items")
    product = relationship("Product")
    dish = relationship("Dish")
