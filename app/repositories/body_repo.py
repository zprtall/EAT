from app.models.body_param import BodyParam

class BodyRepo:

    def get_body(self, session, user):
        return session.query(BodyParam).filter(
            BodyParam.user_id == user.id
        ).all()

    def get_one_body(self, session, user, body_id):
        return (
            session.query(BodyParam)
            .filter(
                BodyParam.user_id == user.id,
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