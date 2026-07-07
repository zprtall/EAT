from sqladmin import Admin
from app.admin.auth import AdminAuth
from app.admin.views import (
    Users,

)


def setup_admin(app, engine):

    admin = Admin(
        app,
        engine,
        authentication_backend=AdminAuth(
            secret_key="SUPER_SECRET"
        )
    )

    admin.add_view(Users)


    return admin