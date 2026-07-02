from fastapi import HTTPException
from app.models.target import NutritionTarget
from app.repositories.target_repo import NutritionRepository

class NutritionService:

    def __init__(self, repo: NutritionRepository):
        self.repo = repo

    def _get_or_create(self, session, user_id: int):
        target = self.repo.get_by_user(session, user_id)
        if not target:
            target = NutritionTarget(user_id=user_id)
            target = self.repo.create(session, target)
        return target

    def update_calories(self, session, user_id: int, value: float):
        if value <= 0:
            raise HTTPException(400, "calories must be > 0")
        target = self._get_or_create(session, user_id)
        target.calories = value
        return self.repo.save(session, target)

    def update_proteins(self, session, user_id: int, value: float):
        if value <= 0:
            raise HTTPException(400, "proteins must be > 0")
        target = self._get_or_create(session, user_id)
        target.proteins = value
        return self.repo.save(session, target)

    def update_fats(self, session, user_id: int, value: float):
        if value <= 0:
            raise HTTPException(400, "fats must be > 0")
        target = self._get_or_create(session, user_id)
        target.fats = value
        return self.repo.save(session, target)

    def update_carbs(self, session, user_id: int, value: float):
        if value <= 0:
            raise HTTPException(400, "carbs must be > 0")
        target = self._get_or_create(session, user_id)
        target.carbs = value
        return self.repo.save(session, target)
