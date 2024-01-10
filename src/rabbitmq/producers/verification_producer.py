from src.rabbitmq.connection import ConnectionToRabbitMQ


def producer_verification_notification(email: str, name: str, link: str) -> None:
    with ConnectionToRabbitMQ() as channel:
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="verification", durable=True)
        channel.queue_bind(exchange="notifications", queue="verification", routing_key="verification-notification")

        channel.basic_publish(
            exchange="notifications",
            routing_key="verification-notification",
            body=str(
                {
                    "email": email,
                    "name": name,
                    "link": link,
                }
            ),
        )
