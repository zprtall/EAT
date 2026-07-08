from app.models.dish import Dish
from app.models.product import Product

class LibraryRepo:
    def get_dishes(self, session, user, search_query: str |None = None):
        q = session.query(Dish).filter(Dish.user_id == user.id)
        if search_query:
            q = q.filter(Dish.name.ilike(f"%{search_query}%"))
        return q.all()

    def get_products(self, session, user, search_query: str | None = None):
        q = session.query(Product).filter(Product.user_id == user.id)
        if search_query:
            q = q.filter(Product.name.ilike(f"%{search_query}%"))
        return q.all()
