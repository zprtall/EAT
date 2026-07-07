from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.core.database import get_session
from app.repositories.library_repo import LibraryRepo
from app.services.library_services import LibraryService
from app.auth.dependencie import get_current_user

router = APIRouter(prefix="/library")

def get_library_service():
    return LibraryService(LibraryRepo())

@router.get("/")
def get_library(
        search: str | None = None,
        user=Depends(get_current_user),
        session: Session = Depends(get_session),
        service: LibraryService = Depends(get_library_service)
):
    return service.get_library(session, user, search)
