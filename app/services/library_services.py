from app.repositories.library_repo import LibraryRepo


class LibraryService:
    def __init__(self, repo: LibraryRepo):
        self.repo = repo

    def get_library(self, session, user_id: int, search_query: str = None):
        dishes = self.repo.get_dishes(session, user_id, search_query)
        products = self.repo.get_products(session, user_id, search_query)
        result = []
        for d in dishes:
            result.append({
                "id": d.id,
                "name": d.name,
                "calories": d.calories,
                "proteins": d.proteins,
                "fats": d.fats,
                "carbs": d.carbs,
                "is_finished": d.is_finished
            })

        for p in products:
            result.append({
                "id": p.id,
                "name": p.name,
                "calories": p.calories,
                "proteins": p.proteins,
                "fats": p.fats,
                "carbs": p.carbs,
            })
        return result
