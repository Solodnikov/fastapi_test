# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # app_title: str = 'Бронирование переговорок'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
