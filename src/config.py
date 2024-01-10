import redis
from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    LOGGING_LEVEL: str

    JWT_SECRET_KEY: str
    JWT_TOKEN_EXPIRES: int

    EMAIL_UUID_EXPIRATION: int

    REDIS_HOST: str
    REDIS_PORT: int

    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    RABBITMQ_HOST: str
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_PORT: int

    FRONTEND_DOMAIN: str
    AUTHENTICATION_DOMAIN: str

    GRPC_PORT: int

    @property
    def SQLALCHEMY_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
        )

    class Config:
        env_file = ".env"


# ENVIRONMENT VARIABLES
settings = Settings()

# LOGGER
logger.add("authentication.log", rotation="1 week", format="{level} | {time} | {message}", level=settings.LOGGING_LEVEL)

# REDIS
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
