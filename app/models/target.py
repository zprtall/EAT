from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, ForeignKey

class NutritionDailyTarget(Base):
    __tablename__ = "nutrition_daily_target"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    calories: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    proteins: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    fats: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    carbs: Mapped[float] = mapped_column(Float, nullable=False, default=0)

    user = relationship("User", back_populates="nutrition_daily_target")