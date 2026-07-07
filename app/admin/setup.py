from sqladmin import Admin

from app.admin.views import (
    Users,

)


def setup_admin(app, engine):

    admin = Admin(
        app,
        engine
    )

    admin.add_view(Users)


    return admin