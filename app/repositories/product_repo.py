from app.models.product import Product


class ProductRepo:

    def get_product(self, session, user_id: int, product_id: int):
        return session.query(Product).filter(
            Product.product_id == product_id,
            Product.user_id == user_id
        ).first()

    def create_products(self, session, product):
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    def delete_product(self, session, product):
        session.delete(product)
        session.commit()

    def update_product(self, session, product):
        session.commit()
        session.refresh(product)
        return product