from pydantic import BaseModel


class JWTTokenSchema(BaseModel):
    token: str
