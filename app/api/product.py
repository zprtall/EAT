from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.schemas.product import Product
from app.repositories.product_repo import ProductRepo
from app.services.product_service import ProductService
from app.core.database import get_session
from app.auth.dependencie import get_current_user

router = APIRouter(prefix="/product")

def get_product_service():
    return ProductService(ProductRepo())


@router.post("/add/")
def add_product(
        data: Product,
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: ProductService = Depends(get_product_service)
):
    return service.add_product(session, user, data)

@router.delete("/delete/")
def del_product(
        product_id: int,
        user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: ProductService = Depends(get_product_service)
):
    return service.delete_product(session, product_id, user)

@router.put("/update/")
def update_product(
        product_id: int,
        data: Product,
    user = Depends(get_current_user),
        session: Session = Depends(get_session),
        service: ProductService = Depends(get_product_service)
):
    return service.update_product(session, user, product_id, data)
