from pydantic import BaseModel


class TokenSchema(BaseModel):
    token: str  # TODO сделать валидацию, чтобы это был жвт токен, а не строка
