from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


str16 = Annotated[str, 16]
str32 = Annotated[str, 32]
str64 = Annotated[str, 64]


class Base(DeclarativeBase):
    """Base model class from which other models inherit"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    type_annotation_map = {
        str16: String(16),
        str32: String(32),
        str64: String(64),
    }
