from pydantic import BaseModel, EmailStr


class UserLoginRequestSchema(BaseModel):
    email: EmailStr
    password: str
