from pydantic import BaseModel, Field

class NutritionDailyTarget(BaseModel):
    user_id: int
    id: int

    calories: float = Field(gt=0)
    proteins: float = Field(gt=0)
    fats: float = Field(gt=0)
    carbs: float = Field(gt=0)
