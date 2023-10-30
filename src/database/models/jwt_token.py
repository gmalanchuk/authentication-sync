from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base
from src.database.models.mixin import TimeStampMixin


class TokenWhiteList(Base, TimeStampMixin):
    token: Mapped[str] = mapped_column(type_=String, index=True, nullable=False)
