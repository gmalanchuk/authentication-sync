from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import logger
from src.database.models.base import Base
from src.database.session import async_session
from src.repositories.base.abstract import AbstractRepository


class StartTransaction:
    async def __aenter__(self):
        self.session = async_session()
        logger.info("Transaction has been opened")
        return self.session

    async def __aexit__(self, *args):
        logger.info("The transaction was a rollback")
        await self.session.rollback()
        await self.session.close()


class PostgresRepository(AbstractRepository):
    model = type[Base]

    async def add_one(self, data: dict):
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.__table__)
            res = await session.execute(stmt)
            await session.commit()
            return dict(res.fetchone()._mapping)

    async def transaction_add_one(self, session: AsyncSession, data: dict):
        """For use only in the StartTransaction context manager"""
        stmt = insert(self.model).values(**data).returning(self.model.__table__)
        res = await session.execute(stmt)
        return dict(res.fetchone()._mapping)

    async def get_one(self, model_field: str, value: str):
        async with async_session() as session:
            field = getattr(self.model, model_field)
            query = select(self.model).where(field == value)
            return (await session.execute(query)).scalars().first()
