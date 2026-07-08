from fastapi import APIRouter, Depends
import datetime
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.meal_repo import MealRepository
from app.schemas.meal import MealCreate, DayResponse
from app.services.meal_services import MealService
from app.auth.dependencie import get_current_user

router = APIRouter(prefix="/meals")


def get_meal_service():
    return MealService(MealRepository())


@router.get("/", response_model=DayResponse)
def get_day(
    date: datetime.date,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: MealService = Depends(get_meal_service)
):
    return service.get_day(session, user, date)


@router.post("/add/", response_model=MealCreate)
def add_meal(
    data: MealCreate,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: MealService = Depends(get_meal_service)
):
    return service.add_meal(session, user, data)


@router.delete("/delete/")
def delete_meal(
    meal_id: int,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: MealService = Depends(get_meal_service)
):
    return service.delete_meal(session, meal_id, user)

@router.put("/update/", response_model=MealCreate)
def update_meal(
    meal_id: int,
    data: MealCreate,
    user = Depends(get_current_user),
    session: Session = Depends(get_session),
    service: MealService = Depends(get_meal_service)
):
    return service.update_meal(session, meal_id, user, data)
