from pydantic import BaseModel, Field

class NutritionDailyTarget(BaseModel):
    user_id: int
    id: int

    calories: float = Field(ge=0)
    proteins: float = Field(ge=0)
    fats: float = Field(ge=0)
    carbs: float = Field(ge=0)
