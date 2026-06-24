import datetime
from pydantic import BaseModel
from .product import Product
from .dish import Dish

class MealType:
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

class Meal(BaseModel):
    date: datetime.date
    meal_type: MealType
    time: datetime.time
    food: Product | Dish   #будет браться из Библиотеки Продуктов/блюд