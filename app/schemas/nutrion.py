from pydantic import BaseModel, Field

class NutritionTarget(BaseModel):
    user_id: int
    calories: float = Field(gt=0)
    protein: float = Field(gt=0)
    fat: float = Field(gt=0)
    carbs: float = Field(gt=0)
