from pydantic import BaseModel

class NutritionTarget(BaseModel):
    user_id: int
    calories: float
    protein: float
    fat: float
    carbs: float