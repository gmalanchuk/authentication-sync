from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base, str16, str32, str64
from src.database.models.mixin import TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    username: Mapped[str16] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str32]
    hashed_password: Mapped[str64] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False, default=False)
