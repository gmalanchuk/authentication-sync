from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


str16 = Annotated[int, 16]
str32 = Annotated[int, 32]
str64 = Annotated[int, 64]


class Base(DeclarativeBase):
    """Base model class from which other models inherit"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    type_annotation_map = {
        str16: String(16),
        str32: String(32),
        str64: String(64),
    }
