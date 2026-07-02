from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.dish_repo import DishRepo
from app.schemas.dish import Dish as DishSchema
from app.services.dish_services import DishService

router = APIRouter(prefix="/dish/")


def get_dish_service():
    return DishService(DishRepo())


@router.get("/{dish_id}")
def get_dish(
    dish_id: int,
    session: Session = Depends(get_session),
    service: DishService = Depends(get_dish_service)
):
    return service.get_dish(session, dish_id)


@router.post("/add/")
def add_dish(
        data: DishSchema,
        user_id: int,
        finish: bool,
        session: Session = Depends(get_session),
        service: DishService = Depends(get_dish_service)
):
    return service.add_dish(session, user_id, finish, data)


@router.put("/update/")
def update_dish(
    dish_id: int,
    data: DishSchema,
    finish: bool,
    session: Session = Depends(get_session),
    service: DishService = Depends(get_dish_service)
):
    return service.update_dish(session, dish_id, data, finish)


@router.delete("/{dish_id}")
def delete_dish(
    dish_id: int,
    session: Session = Depends(get_session),
    service: DishService = Depends(get_dish_service)
):
    return service.delete_dish(session, dish_id)