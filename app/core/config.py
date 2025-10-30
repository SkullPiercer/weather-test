from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_TITLE: str
    APP_DESCRIPTION: str
    WEATHER_API_KEY: str

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int
    DB_HOST: str

    @property
    def DB_URL(self):
        return f'sqlite+aiosqlite:///./fastapi.db'

    model_config = SettingsConfigDict(env_file='.env', extra='allow')

@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore
