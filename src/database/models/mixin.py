from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class TimeStampMixin:
    created_at: Mapped[str] = mapped_column(type_=DateTime, index=True, nullable=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(
        type_=DateTime, server_default=func.now(), server_onupdate=func.now(), onupdate=datetime.now
    )
