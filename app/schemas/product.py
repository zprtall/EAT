from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    calories: float
    proteins: float
    fats: float
    carbs: float