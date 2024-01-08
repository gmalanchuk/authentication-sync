from src.database.models import EmailVerification
from src.repositories.base.postgres import PostgresRepository


class EmailRepository(PostgresRepository):
    model = EmailVerification
