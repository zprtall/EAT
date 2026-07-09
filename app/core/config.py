import os
from pydantic_settings import BaseSettings





class Settings(BaseSettings):
    DATABASE_URL: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DEBUG: bool = True

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str

    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
