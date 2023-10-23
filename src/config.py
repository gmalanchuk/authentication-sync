from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    LOGGING_LEVEL: str

    class Config:
        env_file = ".env"


# ENVIRONMENT VARIABLES
settings = Settings()


# LOGGER
logger.add("authentication.log", rotation="1 week", format="{level} | {time} | {message}", level=settings.LOGGING_LEVEL)
