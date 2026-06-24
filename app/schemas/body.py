import datetime
from pydantic import BaseModel

class BodyParam(BaseModel):
    date: datetime.date
    user_id: int
    weight: float
    neck: float
    shoulder: float
    forearm: float
    chest_on_exhale: float
    chest_on_the_inhale: float
    waist: float
    hip: float
    shin: float