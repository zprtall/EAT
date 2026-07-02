from fastapi import HTTPException

from app.repositories.dish_repo import DishRepo
from app.models.dish import Dish as DishModel, Ingredient
from app.schemas.dish import Dish as DishSchema


class DishService:

    def __init__(self, repo: DishRepo):
        self.repo = repo

    def get_dish(self, session, dish_id: int):
        dish = self.repo.get_dish(session, dish_id)
        if not dish:
            raise HTTPException(status_code=404, detail="Блюдо не найдено")
        return dish

    def add_dish(self, session, user_id: int, finish: bool, data: DishSchema):
        dish = DishModel(
            user_id=user_id,
            name=data.name,
            weight_finish_dish=None if finish else data.weight_finish_dish,
            is_finished=finish
        )

        for ing in data.ingredients:
            dish.ingredients.append(
                Ingredient(
                    weight=ing.weight,
                    calories=ing.calories,
                    proteins=ing.proteins,
                    fats=ing.fats,
                    carbs=ing.carbs
                )
            )

        if finish:
            dish.weight_finish_dish = sum(i.weight for i in dish.ingredients)
            calories, proteins, fats, carbs = self.calculate_dish_kbju(dish, True)

            dish.calories = calories
            dish.proteins = proteins
            dish.fats = fats
            dish.carbs = carbs

        return self.repo.add_dish(session, dish)

    def update_dish(self, session, dish_id: int, data: DishSchema, finish: bool):
        dish = self.repo.get_dish(session, dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="Блюдо не найдено")

        dish.name = data.name
        dish.is_finished = finish

        dish.ingredients.clear()

        for ing in data.ingredients:
            dish.ingredients.append(
                Ingredient(
                    weight=ing.weight,
                    calories=ing.calories,
                    proteins=ing.proteins,
                    fats=ing.fats,
                    carbs=ing.carbs
                )
            )

        if finish:
            dish.weight_finish_dish = sum(i.weight for i in dish.ingredients)
            calories, proteins, fats, carbs = self.calculate_dish_kbju(dish, True)
        else:
            dish.weight_finish_dish = data.weight_finish_dish

            if dish.weight_finish_dish:
                calories, proteins, fats, carbs = self.calculate_dish_kbju(dish, False)
            else:
                calories = proteins = fats = carbs = None

        dish.calories = calories
        dish.proteins = proteins
        dish.fats = fats
        dish.carbs = carbs

        return self.repo.update_dish(session, dish)

    def delete_dish(self, session, dish_id: int):
        dish = self.repo.get_dish(session, dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="Блюдо не найдено")

        self.repo.delete_dish(session, dish)
        return {"message": "Блюдо удалено"}

    def calculate_dish_kbju(self, dish: DishModel, finish: bool):
        if finish:
            weight_finish_dish = sum(ing.weight for ing in dish.ingredients)
        else:
            if not dish.weight_finish_dish:
                raise ValueError("Не указан вес готового блюда")
            weight_finish_dish = dish.weight_finish_dish

        if weight_finish_dish == 0:
            raise ValueError("Вес блюда не может быть 0")

        total_calories = total_proteins = total_fats = total_carbs = 0

        for ing in dish.ingredients:
            factor = ing.weight / 100
            total_calories += ing.calories * factor
            total_proteins += ing.proteins * factor
            total_fats += ing.fats * factor
            total_carbs += ing.carbs * factor

        coef = 100 / weight_finish_dish

        return (
            round(total_calories * coef, 2),
            round(total_proteins * coef, 2),
            round(total_fats * coef, 2),
            round(total_carbs * coef, 2),
        )