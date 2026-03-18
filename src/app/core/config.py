from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Relation Database Settings
    POSTGRES_AUTH_URL: str
    POSTGRES_AUTH_USER: str
    POSTGRES_AUTH_PASSWORD: str
    POSTGRES_AUTH_PORT: int
    POSTGRES_AUTH_DB: str
    POSTGRES_AUTH_HOST: str

    # Auth
    ACCESS_TOKEN_LIFETIME_S: int
    RESET_PASSWORD_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str
    JWT_SECRET: str
    ALGO: str
    AUTH_SERVICE_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore


settings = get_settings()
