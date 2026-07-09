import os
from pydantic_settings import BaseSettings

TELEGRAM_BOT_TOKEN = os.getenv("8866695900:AAGncgC7I-OT96mXK1BYfx_p85zUaN9jZz0")




class Settings(BaseSettings):
    DATABASE_URL: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DEBUG: bool = True

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()