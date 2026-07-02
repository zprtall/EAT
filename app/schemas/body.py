import datetime
from pydantic import BaseModel, Field


class BodyParam(BaseModel):
    date: datetime.date
    user_id: int
    weight: float = Field(gt=0)
    neck: float = Field(gt=0)
    shoulder: float = Field(gt=0)
    forearm: float = Field(gt=0)
    chest_on_exhale: float = Field(gt=0)
    chest_on_the_inhale: float = Field(gt=0)
    waist: float = Field(gt=0)
    hip: float = Field(gt=0)
    shin: float = Field(gt=0)