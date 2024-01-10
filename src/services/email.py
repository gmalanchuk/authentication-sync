import json

from starlette.responses import JSONResponse

from src.config import settings
from src.rabbitmq.producers.verification_producer import producer_verification_notification
from src.repositories.email import EmailRepository


class EmailHTTPService:
    pass


class EmailRabbitMQService:
    def __init__(self) -> None:
        self.email_repository = EmailRepository()

    async def email_verification_notification(self, response: JSONResponse) -> None:
        data = json.loads(response.body.decode("utf-8"))  # converting a byte string to a dictionary

        email_verification_obj = await self.email_repository.get_one(model_field="user_id", value=data["id"])

        link = f"{settings.AUTHENTICATION_DOMAIN}/email/verification/{email_verification_obj.code}/"
        producer_verification_notification(email=data["email"], name=data["name"], link=link)
