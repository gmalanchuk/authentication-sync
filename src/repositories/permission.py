from src.database.models import User
from src.repositories.base.postgres import PostgresRepository


class PermissionRepository(PostgresRepository):
    model = User
