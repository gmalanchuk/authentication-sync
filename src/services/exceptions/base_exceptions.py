from starlette import status

from src.enums.tag import TagEnum
from src.services.exceptions.grpc_exceptions import GRPCExceptions
from src.services.exceptions.http_exceptions import HTTPExceptions


class BaseExceptions:
    def __init__(self, tag: TagEnum) -> None:
        self.tag = tag

    @staticmethod
    async def get_exception_tag(tag):
        tags = {TagEnum.HTTP: HTTPExceptions(), TagEnum.GRPC: GRPCExceptions()}
        return tags[tag]

    async def is_invalid(self, value1: str, value2: str | None = None):
        tag_exception = await self.get_exception_tag(self.tag)
        value2 = f"or {value2} " if value2 else ""
        detail = f"{value1} {value2}is invalid"
        status_code = status.HTTP_401_UNAUTHORIZED
        return await tag_exception.is_invalid(detail, status_code)

    async def has_expired(self, value: str):
        tag_exception = await self.get_exception_tag(self.tag)
        detail = f"{value} has expired"
        status_code: int = status.HTTP_401_UNAUTHORIZED
        return await tag_exception.has_expired(detail, status_code)

    async def must_be_confirmed(self, value: str):
        tag_exception = await self.get_exception_tag(self.tag)
        detail = f"To perform this action, your {value} must be confirmed"
        status_code = status.HTTP_401_UNAUTHORIZED
        return await tag_exception.must_be_confirmed(detail, status_code)

    async def login_required(self):
        tag_exception = await self.get_exception_tag(self.tag)
        detail = "Login required"
        status_code = status.HTTP_401_UNAUTHORIZED
        return await tag_exception.login_required(detail, status_code)

    async def not_found(self, value: str):
        tag_exception = await self.get_exception_tag(self.tag)
        detail = f"{value} not found"
        status_code = status.HTTP_404_NOT_FOUND
        return await tag_exception.not_found(detail, status_code)
