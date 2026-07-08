import datetime
from fastapi import HTTPException

from app.models.target import NutritionDailyTarget
from app.models.meal import Meal, MealItem
from app.repositories.meal_repo import MealRepository
from app.schemas.meal import MealCreate


class MealService:

    def __init__(self, repo: MealRepository):
        self.repo = repo

    def get_day(self, session, user, date: datetime.date):
        meals = self.repo.get_by_meal_date(session, user.id, date)

        result_meals = []
        day_cal = day_p = day_f = day_c = 0

        for meal in meals:
            items_out = []
            m_cal = m_p = m_f = m_c = 0

            for item in meal.items:
                if item.product:
                    name = item.product.name
                    factor = item.grams / 100
                    cal = item.product.calories * factor
                    p = item.product.proteins * factor
                    f = item.product.fats * factor
                    c = item.product.carbs * factor
                else:
                    name = item.dish.name
                    factor = item.grams / 100
                    cal = item.dish.calories * factor
                    p = item.dish.proteins * factor
                    f = item.dish.fats * factor
                    c = item.dish.carbs * factor

                m_cal += cal
                m_p += p
                m_f += f
                m_c += c

                items_out.append({
                    "name": name,
                    "grams": item.grams,
                    "calories": cal,
                    "proteins": p,
                    "fats": f,
                    "carbs": c
                })

            day_cal += m_cal
            day_p += m_p
            day_f += m_f
            day_c += m_c

            result_meals.append({
                "meal_id": meal.meal_id,
                "time": meal.time,
                "type": meal.type,
                "items": items_out,
                "total_calories": m_cal,
                "total_proteins": m_p,
                "total_fats": m_f,
                "total_carbs": m_c,
            })

        target = session.query(NutritionDailyTarget).filter_by(user_id=user.id).first()

        return {
            "summary": {
                "calories": day_cal,
                "proteins": day_p,
                "fats": day_f,
                "carbs": day_c,
            },
            "target": {
                "calories": target.calories if target else 0,
                "proteins": target.proteins if target else 0,
                "fats": target.fats if target else 0,
                "carbs": target.carbs if target else 0,
            },
            "meals": result_meals
        }

    def add_meal(self, session, user, data: MealCreate):
        meal = Meal(
            user_id=user.id,
            date=data.date,
            time=data.time,
            type=data.type
        )

        items = []

        for item in data.items:
            if not item.product_id and not item.dish_id:
                raise HTTPException(status_code=400, detail="Нужно указать продукт или блюдо")

            meal_item = MealItem(
                product_id=item.product_id,
                dish_id=item.dish_id,
                grams=item.grams
            )
            items.append(meal_item)

        meal.items = items

        return self.repo.create(session, meal)

    def delete_meal(self, session, meal_id: int, user):
        meal = self.repo.get_meal(session, meal_id, user.id)

        if not meal:
            raise HTTPException(status_code=404, detail="приём пищи не найден")

        self.repo.delete_meal(session, meal)

    def update_meal(self, session, meal_id: int, user, data: MealCreate):
        meal = self.repo.get_meal(session, meal_id, user.id)
        if not meal:
            raise HTTPException(status_code=404, detail="приём пищи не найден")
        meal.date = data.date
        meal.time = data.time
        meal.type = data.type
        meal.items.clear()
        new_items = []
        for item in data.items:
            if not item.product_id and not item.dish_id:
                raise HTTPException(status_code=400, detail="Нужно указать продукт или блюдо")
            meal_item = MealItem(
                product_id=item.product_id,
                dish_id=item.dish_id,
                grams=item.grams
            )
            new_items.append(meal_item)
        meal.items = new_items
        return self.repo.update_meal(session, meal)
