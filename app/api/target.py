from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.target_repo import NutritionRepository
from app.services.target_service import NutritionService
from app.auth.dependencie import get_current_user

router = APIRouter(prefix="target")

def get_nutrition_service():
    return NutritionService(NutritionRepository())

@router.put("/calories/")
def update_calories(
    value: float,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_calories(session, user, value)


@router.put("/proteins/")
def update_proteins(
    value: float,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_proteins(session, user, value)


@router.put("/fats/")
def update_fats(
    value: float,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_fats(session, user, value)


@router.put("/carbs/")
def update_carbs(
    value: float,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_carbs(session, user, value)