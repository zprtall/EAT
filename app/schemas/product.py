from pydantic import BaseModel, Field


class Product(BaseModel):
    user_id: int
    name: str = Field(max_length=15)
    calories: float = Field(gt=0)
    proteins: float = Field(ge=0)
    fats: float = Field(ge=0)
    carbs: float = Field(ge=0)