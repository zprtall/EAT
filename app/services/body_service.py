from fastapi import HTTPException

from app.repositories.body_repo import BodyRepo
from app.models.body_param import BodyParam as BodyParamModel
from app.schemas.body import BodyParam as BodyParamSchema


class BodyService:

    def __init__(self, repo: BodyRepo):
        self.repo = repo

    def get_body(self, session, user_id: int):
        return self.repo.get_body(session, user_id)

    def get_one_body(self, session, user_id: int, body_id: int):
        body = self.repo.get_one_body(session, user_id, body_id)
        if not body:
            raise HTTPException(status_code=404, detail="параметры тела не найдены")
        return body

    def add_body(self, session, data: BodyParamSchema, user_id: int):
        param = BodyParamModel(
            user_id=user_id,
            date=data.date,
            weight=data.weight,
            neck=data.neck,
            shoulder=data.shoulder,
            forearm=data.forearm,
            chest_on_exhale=data.chest_on_exhale,
            chest_on_the_inhale=data.chest_on_the_inhale,
            waist=data.waist,
            hip=data.hip,
            shin=data.shin,
        )
        return self.repo.add_body(session, param)

    def delete_body(self, session, body_id: int, user_id: int):
        body = self.get_one_body(session, user_id, body_id)
        self.repo.delete_body(session, body)

    def update_body(self, session, body_id: int, user_id: int, data: BodyParamSchema):
        body = self.get_one_body(session, user_id, body_id)
        for field, value in data.model_dump().items():
            setattr(body, field, value)
        return self.repo.update_body(session, body)
