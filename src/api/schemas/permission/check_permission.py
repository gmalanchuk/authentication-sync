from typing import NoReturn

from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from starlette import status


class TokenSchema(BaseModel):
    token: str

    @field_validator("token")
    def validate_token(cls, token: str) -> str | NoReturn:
        try:
            _, _, _ = token.split(".")
        except ValueError:
            raise HTTPException(detail="Invalid JWT token format", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return token
