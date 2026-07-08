from fastapi import HTTPException

from app.repositories.product_repo import ProductRepo
from app.models.product import Product as ProductModel
from app.schemas.product import Product as ProductSchema


class ProductService:

    def __init__(self, repo: ProductRepo):
        self.repo = repo

    def add_product(self, session, user, data: ProductSchema):
        product = ProductModel(
            user_id=user.id,
            name=data.name,
            calories=data.calories,
            proteins=data.proteins,
            fats=data.fats,
            carbs=data.carbs
        )
        return self.repo.create_products(session, product)

    def get_product(self, session, user, product_id: int):
        return self.repo.get_product(session, user.id, product_id)

    def delete_product(self, session, product_id: int, user):
        product = self.get_product(session, user, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Продукт не найден")
        self.repo.delete_product(session, product)

    def update_product(self, session, user, product_id: int, data: ProductSchema):
        product = self.get_product(session, user, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Продукт не найден")
        for field, value in data.model_dump().items():
            setattr(product, field, value)
        return self.repo.update_product(session, product)