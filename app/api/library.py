from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.database import get_session
from app.repositories.library_repo import LibraryRepo
from app.services.library_services import LibraryService

router = APIRouter(prefix="/library")

def get_library_service():
    return LibraryService(LibraryRepo())

@router.get("/")
def get_library(
        user_id: int,
        search: str | None = None,
        session: Session = Depends(get_session),
        service: LibraryService = Depends(get_library_service)
):
    return service.get_library(session, user_id, search)
