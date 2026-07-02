from app.models.dish import Dish

class DishRepo:
    def add_dish(self, session, dish):
        session.add(dish)
        session.commit()
        session.refresh(dish)
        return dish

    def get_dish(self, session, dish_id: int):
        return session.query(Dish).filter(Dish.id == dish_id).first()

    def delete_dish(self, session, dish):
        session.delete(dish)
        session.commit()

    def update_dish(self, session, dish):
        session.commit()
        session.refresh(dish)