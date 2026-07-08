from pydantic import BaseModel, Field

class NutritionDailyTarget(BaseModel):
    user_id: int
    id: int
    calories: float = Field(gt=0)
    protein: float = Field(gt=0)
    fat: float = Field(gt=0)
    carbs: float = Field(gt=0)
