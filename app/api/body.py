from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.body_repo import BodyRepo
from app.schemas.body import BodyParam as BodyParamSchema
from app.services.body_service import BodyService

router = APIRouter(prefix="/body/")


def get_body_service():
    return BodyService(BodyRepo())


@router.get("/")
def get_body(
        user_id: int,
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.get_body(session, user_id)


@router.post("/add/")
def add_body(
        data: BodyParamSchema,
        user_id: int,
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.add_body(session, data, user_id)


@router.delete("/delete/")
def del_body(
        body_id: int,
        user_id: int,
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.delete_body(session, body_id, user_id)


@router.put("/update/")
def update_body(
        user_id: int,
        body_id: int,
        data: BodyParamSchema,
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.update_body(session, body_id, user_id, data)