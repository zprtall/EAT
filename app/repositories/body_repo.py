from app.models.body_param import BodyParam

class BodyRepo:

    def get_body(self, session, user_id):
        return session.query(BodyParam).filter(
            BodyParam.user_id == user_id
        ).all()

    def get_one_body(self, session, user_id: int, body_id: int):
        return (
            session.query(BodyParam)
            .filter(
                BodyParam.user_id == user_id,
                BodyParam.id == body_id
            )
            .first()
        )

    def add_body(self, session, param):
        session.add(param)
        session.commit()
        session.refresh(param)
        return param

    def delete_body(self, session, body):
        session.delete(body)
        session.commit()

    def update_body(self, session, body):
        session.commit()
        session.refresh(body)
        return body