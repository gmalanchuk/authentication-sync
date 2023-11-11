from typing import NoReturn

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from starlette import status


class UserRegistrationRequestSchema(BaseModel):
    username: str
    email: EmailStr
    name: str
    password: str

    @field_validator("username")
    def validate_username(cls, username: str) -> str | NoReturn:
        if len(username) > 16:
            raise HTTPException(
                detail="Username must be less than 16 characters", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return username

    @field_validator("name")
    def validate_name(cls, name: str) -> str | NoReturn:
        if len(name) > 16:
            raise HTTPException(
                detail="Name must be less than 32 characters", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return name


class UserRegistrationResponseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    name: str
    is_verified: bool
