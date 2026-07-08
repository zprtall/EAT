from sqladmin import ModelView

from app.models.user import User
from app.models.body_param import BodyParam
from app.models.dish import Dish, Ingredient
from app.models.meal import Meal, MealItem
from app.models.product import Product
from app.models.target import NutritionDailyTarget
from app.models.system_settings import SystemSettings
from app.models.user_reminder_settings import UserReminderSettings


class Users(ModelView, model=User):
    column_list = [User.id, User.telegram_id, User.last_reminder_at]
    form_columns = [User.telegram_id, User.last_reminder_at]


class BodyParams(ModelView, model=BodyParam):
    column_list = [
        BodyParam.id,
        BodyParam.user_id,
        BodyParam.date,
        BodyParam.weight,
        BodyParam.waist
    ]
    form_columns = [
        BodyParam.user_id,
        BodyParam.date,
        BodyParam.weight,
        BodyParam.neck,
        BodyParam.shoulder,
        BodyParam.forearm,
        BodyParam.chest_on_exhale,
        BodyParam.chest_on_the_inhale,
        BodyParam.waist,
        BodyParam.hip,
        BodyParam.shin,
    ]


class IngredientsInline(ModelView, model=Ingredient):
    form_columns = [
        Ingredient.weight,
        Ingredient.calories,
        Ingredient.proteins,
        Ingredient.fats,
        Ingredient.carbs,
    ]


class Dishes(ModelView, model=Dish):
    column_list = [
        Dish.dishes_id,
        Dish.name,
        Dish.user_id,
        Dish.is_finished
    ]
    form_columns = [
        Dish.name,
        Dish.user_id,
        Dish.weight_finish_dish,
        Dish.is_finished,
        Dish.calories,
        Dish.proteins,
        Dish.fats,
        Dish.carbs
    ]

    inline_models = [IngredientsInline]


class MealItemsInline(ModelView, model=MealItem):
    form_columns = [
        MealItem.product_id,
        MealItem.dish_id,
        MealItem.grams,
    ]


class Meals(ModelView, model=Meal):
    column_list = [
        Meal.meal_id,
        Meal.user_id,
        Meal.type,
        Meal.date,
        Meal.time
    ]
    form_columns = [
        Meal.user_id,
        Meal.type,
        Meal.date,
        Meal.time,
    ]

    inline_models = [MealItemsInline]


class Products(ModelView, model=Product):
    column_list = [
        Product.product_id,
        Product.name,
        Product.calories
    ]
    form_columns = [
        Product.user_id,
        Product.name,
        Product.calories,
        Product.proteins,
        Product.fats,
        Product.carbs
    ]


class NutritionDailyTargets(ModelView, model=NutritionDailyTarget):
    column_list = [
        NutritionDailyTarget.id,
        NutritionDailyTarget.user_id,
        NutritionDailyTarget.calories
    ]
    form_columns = [
        NutritionDailyTarget.user_id,
        NutritionDailyTarget.calories,
        NutritionDailyTarget.proteins,
        NutritionDailyTarget.fats,
        NutritionDailyTarget.carbs
    ]

class SystemSettingsAdmin(
    ModelView,
    model=SystemSettings
):
    column_list = [
        SystemSettings.reminders_enabled
    ]
    form_columns = [
        SystemSettings.reminders_enabled
    ]

from app.models.user_reminder_settings import UserReminderSettings


class UserReminderSettingsAdmin(
    ModelView,
    model=UserReminderSettings
):

    column_list = [
        UserReminderSettings.user_id,
        UserReminderSettings.reminders_enabled
    ]


    form_columns = [
        UserReminderSettings.user_id,
        UserReminderSettings.reminders_enabled
    ]

