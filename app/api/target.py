from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.target_repo import NutritionRepository
from app.services.target_service import NutritionService

router = APIRouter(prefix="target")

def get_nutrition_service():
    return NutritionService(NutritionRepository())

@router.put("/calories/")
def update_calories(
    value: float,
    user_id: int,
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_calories(session, user_id, value)


@router.put("/proteins/")
def update_proteins(
    value: float,
    user_id: int,
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_proteins(session, user_id, value)


@router.put("/fats/")
def update_fats(
    value: float,
    user_id: int,
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_fats(session, user_id, value)


@router.put("/carbs/")
def update_carbs(
    value: float,
    user_id: int,
    session: Session = Depends(get_session),
    service: NutritionService = Depends(get_nutrition_service)
):
    return service.update_carbs(session, user_id, value)