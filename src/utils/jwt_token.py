import base64
import datetime
import hashlib
import json

from src.config import redis_client, settings


class JWTToken:
    @staticmethod
    async def create_token(user_id: dict) -> str:
        header = base64.b64encode(str({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(
            str(
                {
                    "user_id": user_id,
                    "expiration": (
                        datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_TOKEN_EXPIRES)
                    ).strftime("%Y-%m-%d %H:%M:%S"),
                }
            ).encode()
        ).decode()
        signature = hashlib.sha256((header + payload + settings.JWT_SECRET_KEY).encode()).hexdigest()

        jwt_token = f"{header}.{payload}.{signature}"

        data = json.dumps(
            {
                "token": jwt_token,
                "expiration_time": (datetime.datetime.utcnow() + datetime.timedelta(seconds=900)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "disabled": False,
            }
        )

        redis_client.setex(name=str(user_id), time=settings.JWT_TOKEN_EXPIRES, value=data)

        return jwt_token

    @staticmethod
    async def verify_token() -> None:
        # base64.b64decode(payload).decode()
        pass
