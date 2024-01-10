import pika

from src.config import logger, settings


class ConnectionToRabbitMQ:
    def __enter__(self) -> pika.channel:
        credentials = pika.PlainCredentials(username=settings.RABBITMQ_USER, password=settings.RABBITMQ_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.RABBITMQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()
        logger.info("Rabbitmq connection open")
        return self.channel

    def __exit__(self, *args: tuple) -> None:
        self.connection.close()
        logger.info("Rabbitmq connection closed")
