import datetime
from pydantic import BaseModel, model_validator, Field
from enum import Enum

class MealItemOut(BaseModel):
    name: str
    grams: float
    calories: float
    proteins: float
    fats: float
    carbs: float


class MealOut(BaseModel):
    time: datetime.time
    type: str

    items: list[MealItemOut]

    total_calories: float
    total_proteins: float
    total_fats: float
    total_carbs: float


class DaySummary(BaseModel):
    calories: float
    proteins: float
    fats: float
    carbs: float


class DayResponse(BaseModel):
    summary: DaySummary
    target: DaySummary
    meals: list[MealOut]

class MealType(str, Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class MealItem(BaseModel):
    date: datetime.date
    time: datetime.time
    user_id: int
    type: MealType
    product_id: int | None = None
    dish_id: int | None = None

    @model_validator(mode="after")
    def validate_item(self):
        if not self.product_id and not self.dish_id:
            raise ValueError("Нужно указать product_id или dish_id")

        if self.product_id and self.dish_id:
            raise ValueError("Нельзя указывать и product_id и dish_id")

        return self

class MealItemCreate(BaseModel):
    product_id: int | None = None
    dish_id: int | None = None
    grams: float

class MealCreate(BaseModel):
    date: datetime.date
    time: datetime.time
    type: str
    items: list[MealItemCreate]