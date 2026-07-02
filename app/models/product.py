from app.models.models import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=False)
    proteins: Mapped[float] = mapped_column(Float, nullable=False)
    fats: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)