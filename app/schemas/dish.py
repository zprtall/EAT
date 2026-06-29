from typing import Optional

from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    dish_id: int
    weight: float = Field(gt=0)
    calories: float = Field(go=0)
    proteins: float = Field(ge=0)
    fats: float = Field(ge=0)
    carbs: float = Field(ge=0)

class Dish(BaseModel):
    name: str = Field(max_length=20)
    user_id: int
    dish_id: int
    weight_finish_dish: Optional[float] = Field(gt=0, default=None)
    ingredient: list[Ingredient]
