import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, Time, ForeignKey


class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body_params = relationship("BodyParam", back_populates="user")
    dishes = relationship("Dish", back_populates="user")
    meal_items = relationship("MealItem", back_populates="user")
    nutrition_target = relationship("NutritionTarget", back_populates="user", uselist=False)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    proteins: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)


class BodyParam(Base):
    __tablename__ = "body_params"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    neck: Mapped[float] = mapped_column(Float, nullable=False)
    shoulder: Mapped[float] = mapped_column(Float, nullable=False)
    forearm: Mapped[float] = mapped_column(Float, nullable=False)
    chest_on_exhale: Mapped[float] = mapped_column(Float, nullable=False)
    chest_on_the_inhale: Mapped[float] = mapped_column(Float, nullable=False)
    waist: Mapped[float] = mapped_column(Float, nullable=False)
    hip: Mapped[float] = mapped_column(Float, nullable=False)
    shin: Mapped[float] = mapped_column(Float, nullable=False)

    user = relationship("User", back_populates="body_params")


class NutritionTarget(Base):
    __tablename__ = "nutrition_target"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    proteins: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)

    user = relationship("User", back_populates="nutrition_target")


class Dish(Base):
    __tablename__ = "dishes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    weight_finish_dish: Mapped[float] = mapped_column(Float, nullable=True)

    user = relationship("User", back_populates="dishes")
    ingredients = relationship(
        "Ingredient",
        back_populates="dish",
        cascade="all, delete-orphan"
    )
    meal_items = relationship("MealItem", back_populates="dish")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id"), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    proteins: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)

    dish = relationship("Dish", back_populates="ingredients")


class MealItem(Base):
    __tablename__ = "meal_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id"), nullable=True)
    dish_id: Mapped[int | None] = mapped_column(ForeignKey("dishes.id"), nullable=True)

    user = relationship("User", back_populates="meal_items")
    dish = relationship("Dish", back_populates="meal_items")
    product = relationship("Product")