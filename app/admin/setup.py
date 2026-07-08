from sqladmin import Admin
from app.admin.auth import AdminAuth
from app.admin.views import (
    Users,
    BodyParams,
    Dishes,
    Meals,
    Products,
    NutritionDailyTargets,
    SystemSettingsAdmin,
    UserReminderSettingsAdmin,
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
    admin.add_view(BodyParams)
    admin.add_view(Dishes)
    admin.add_view(Meals)
    admin.add_view(Products)
    admin.add_view(NutritionDailyTargets)
    admin.add_view(SystemSettingsAdmin)
    admin.add_view(UserReminderSettingsAdmin)

    return admin