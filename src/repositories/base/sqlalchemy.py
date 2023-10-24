from sqlalchemy import insert, select

from src.database.models.base import Base
from src.database.session import async_session
from src.repositories.base.abstract import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model = type[Base]

    async def add_one(self, data: dict):
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.__table__)
            res = await session.execute(stmt)
            await session.commit()
            return dict(res.fetchone()._mapping)

    async def get_one(self, model_field: str, value: str):
        async with async_session() as session:
            field = getattr(self.model, model_field)
            query = select(self.model).where(field == value)
            return (await session.execute(query)).scalars().first()
