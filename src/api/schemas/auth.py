from typing import NoReturn

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


class UserRegistrationRequestSchema(BaseModel):
    username: str
    email: EmailStr
    name: str
    password: str

    @field_validator("username")
    def validate_username(cls, username: str) -> str | NoReturn:
        if len(username) > 16:
            raise HTTPException(detail="Username must be less than 16 characters", status_code=422)
        return username


class UserRegistrationResponseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    name: str
    is_verified: bool
