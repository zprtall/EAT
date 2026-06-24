from pydantic import BaseModel

class Ingredient(BaseModel):
    weight: float
    calories: float
    proteins: float
    fats: float
    carbs: float

class Dish(BaseModel):
    name: str
    weight_finish_dish: float
    ingredient: Ingredient
