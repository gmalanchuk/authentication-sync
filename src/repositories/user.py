from src.database.models import User
from src.repositories.base.postgres import PostgresRepository


class UserRepository(PostgresRepository):
    model = User
