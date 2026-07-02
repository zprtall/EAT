import datetime
from sqlalchemy.orm import joinedload
from app.models.meal import Meal, MealItem


class MealRepository:

    def get_by_meal_date(self, session, user_id: int, date: datetime.date):
        return (
            session.query(Meal)
            .filter(Meal.user_id == user_id, Meal.date == date)
            .options(
                joinedload(Meal.items).joinedload(MealItem.product),
                joinedload(Meal.items).joinedload(MealItem.dish),
            )
            .all()
        )

    def create(self, session, meal):
        session.add(meal)
        session.commit()
        session.refresh(meal)
        return meal

    def get_meal(self, session, meal_id: int, user_id: int):
        return (
            session.query(Meal)
            .filter(Meal.meal_id == meal_id, Meal.user_id == user_id)
            .first()
        )

    def delete_meal(self, session, meal):
        session.delete(meal)
        session.commit()

    def update_meal(self, session, meal):
        session.commit()
        session.refresh(meal)
        return meal