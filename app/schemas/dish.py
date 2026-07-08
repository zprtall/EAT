from typing import Optional

from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    weight: float = Field(gt=0)
    calories: float = Field(ge=0)
    proteins: float = Field(ge=0)
    fats: float = Field(ge=0)
    carbs: float = Field(ge=0)

class Dish(BaseModel):
    user_id: int
    name: str
    weight_finish_dish: Optional[float] = None

    calories: Optional[float] = None
    proteins: Optional[float] = None
    fats: Optional[float] = None
    carbs: Optional[float] = None

    ingredients: list[Ingredient]
