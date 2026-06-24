from pydantic import BaseModel

class Product(BaseModel):
    name: str
    calories: float
    proteins: float
    fats: float
    carbs: float