import datetime
from pydantic import BaseModel, model_validator
from enum import Enum

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