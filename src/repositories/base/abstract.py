from abc import ABC, abstractmethod
from typing import Any, NoReturn


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, *args: Any, **kwargs: Any) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args: Any, **kwargs: Any) -> NoReturn:
        raise NotImplementedError
