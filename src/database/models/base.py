from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base model class from which other models inherit"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
