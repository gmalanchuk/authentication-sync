from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base
from src.database.models.mixin import TimeStampMixin


class EmailVerification(Base, TimeStampMixin):
    __tablename__ = "email_verification"

    code: Mapped[UUID] = mapped_column(nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(column="users.id", ondelete="CASCADE"), nullable=False)
    expiration: Mapped[datetime] = mapped_column(nullable=False)
