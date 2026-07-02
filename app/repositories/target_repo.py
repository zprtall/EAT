from app.models.target import NutritionTarget

class NutritionRepository:

    def get_by_user(self, session, user_id: int):
        return session.query(NutritionTarget).filter_by(user_id=user_id).first()

    def create(self, session, target):
        session.add(target)
        session.commit()
        session.refresh(target)
        return target

    def save(self, session, target):
        session.commit()
        session.refresh(target)
        return target