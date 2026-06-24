from pydantic import BaseModel

class User(BaseModel):
    number_of_calories_per_day: int
    number_of_proteins_per_day: int
    number_of_fats_per_day: int
    number_of_carbohydrates_per_day: int