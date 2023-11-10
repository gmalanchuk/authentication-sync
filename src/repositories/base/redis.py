from src.config import redis_client
from src.repositories.base.abstract import AbstractRepository


class RedisRepository(AbstractRepository):
    async def add_one(self, name: str | int, value: str, time: int = 0):
        if time == 0:
            redis_client.set(name=str(name), value=value)
        else:
            redis_client.setex(name=str(name), value=value, time=time)

    async def get_one(self):
        pass
