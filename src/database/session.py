from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings


engine = create_async_engine(settings.SQLALCHEMY_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
