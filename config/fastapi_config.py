import os

from .config import Config


class FastAPIConfig(Config):
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    JWT_REFRESH_SECRET_KEY = os.environ["JWT_REFRESH_SECRET_KEY"]
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    ALGORITHM = "HS256"
