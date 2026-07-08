import datetime
from pydantic import BaseModel, model_validator
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



class MealItemCreate(BaseModel):
    product_id: int | None = None
    dish_id: int | None = None
    grams: float

class MealCreate(BaseModel):
    date: datetime.date
    time: datetime.time
    type: str
    items: list[MealItemCreate]