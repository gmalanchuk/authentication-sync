from src.database.models import User
from src.repositories.base.sqlalchemy import SQLAlchemyRepository


class AuthRepository(SQLAlchemyRepository):
    model = User
