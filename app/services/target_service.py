from fastapi import HTTPException
from app.models.target import NutritionDailyTarget
from app.repositories.target_repo import NutritionRepository

class NutritionService:

    def __init__(self, repo: NutritionRepository):
        self.repo = repo

    def _get_or_create(self, session, user):
        target = self.repo.get_by_user(session, user.id)
        if not target:
            target = NutritionDailyTarget(user_id=user.id)
            target = self.repo.create(session, target)
        return target

    def update_calories(self, session, user, value: float):
        if value <= 0:
            raise HTTPException(400, "calories must be > 0")
        target = self._get_or_create(session, user)
        target.calories = value
        return self.repo.save(session, target)

    def update_proteins(self, session, user, value: float):
        if value <= 0:
            raise HTTPException(400, "proteins must be > 0")
        target = self._get_or_create(session, user)
        target.proteins = value
        return self.repo.save(session, target)

    def update_fats(self, session, user, value: float):
        if value <= 0:
            raise HTTPException(400, "fats must be > 0")
        target = self._get_or_create(session, user)
        target.fats = value
        return self.repo.save(session, target)

    def update_carbs(self, session, user, value: float):
        if value <= 0:
            raise HTTPException(400, "carbs must be > 0")
        target = self._get_or_create(session, user)
        target.carbs = value
        return self.repo.save(session, target)