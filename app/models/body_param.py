from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, Date, ForeignKey
import datetime

class BodyParam(Base):
    __tablename__ = "body_params"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    neck: Mapped[float] = mapped_column(Float, nullable=False)
    shoulder: Mapped[float] = mapped_column(Float, nullable=False)
    forearm: Mapped[float] = mapped_column(Float, nullable=False)
    chest_on_exhale: Mapped[float] = mapped_column(Float, nullable=False)
    chest_on_the_inhale: Mapped[float] = mapped_column(Float, nullable=False)
    waist: Mapped[float] = mapped_column(Float, nullable=False)
    hip: Mapped[float] = mapped_column(Float, nullable=False)
    shin: Mapped[float] = mapped_column(Float, nullable=False)

    user = relationship("User", back_populates="body_params")