from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "63531905db120c8c92fbb17b9e103823462fa3f320234635f086b197a1ef32d2"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # Database
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///./mail_api.db"

    class Config:
        case_sensitive = True


settings = Settings()
