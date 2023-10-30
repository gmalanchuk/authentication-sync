from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    LOGGING_LEVEL: str

    JWT_SECRET_KEY: str
    JWT_TOKEN_EXPIRES: int

    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str

    @property
    def SQLALCHEMY_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


# ENVIRONMENT VARIABLES
settings = Settings()


# LOGGER
logger.add("authentication.log", rotation="1 week", format="{level} | {time} | {message}", level=settings.LOGGING_LEVEL)
