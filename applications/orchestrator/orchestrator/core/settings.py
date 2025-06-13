import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENVIRONMENT', 'develop')}", env_file_encoding="utf-8"
    )
    CELERY_BROKER_URL: str
    CELERY_BACKEND_URL: str
    ORCHESTRATOR_DB_URL: str


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
