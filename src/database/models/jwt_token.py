from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base
from src.database.models.mixin import TimeStampMixin


class TokenWhiteList(Base, TimeStampMixin):
    __tablename__ = "whitelist"

    token: Mapped[str] = mapped_column(index=True, nullable=False)
