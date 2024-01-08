from src.rabbitmq.connection import ConnectionToRabbitMQ


def producer_link_notification(username: str, link: str) -> None:
    with ConnectionToRabbitMQ() as channel:
        channel.exchange_declare(exchange="notifications", exchange_type="direct", durable=True)
        channel.queue_declare(queue="link", durable=True)
        channel.queue_bind(exchange="notifications", queue="link", routing_key="link-notification")

        channel.basic_publish(
            exchange="notifications",
            routing_key="link-notification",
            body=str(
                {
                    "username": username,
                    "link": link,
                }
            ),
        )
