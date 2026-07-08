from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.repositories.body_repo import BodyRepo
from app.schemas.body import BodyParam
from app.services.body_service import BodyService
from app.auth.dependencie import get_current_user

router = APIRouter(prefix="/body")


def get_body_service():
    return BodyService(BodyRepo())


@router.get("/", response_model=BodyParam)
def get_body(
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.get_body(session, user)


@router.post("/add/", response_model=BodyParam)
def add_body(
        data: BodyParam,
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.add_body(session, data, user)


@router.delete("/delete/", response_model=BodyParam)
def del_body(
        body_id: int,
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.delete_body(session, body_id, user)


@router.put("/update/", response_model=BodyParam)
def update_body(
        body_id: int,
        data: BodyParam,
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: BodyService = Depends(get_body_service)
):
    return service.update_body(session, body_id, user, data)