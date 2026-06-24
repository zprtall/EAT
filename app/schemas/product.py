from pydantic import BaseModel

class Product(BaseModel):
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int