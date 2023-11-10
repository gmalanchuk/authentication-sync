import base64
import datetime
import hashlib
import json

from src.config import settings
from src.repositories.base.redis import RedisRepository


class JWTTokenSaveToRedis:
    def __init__(self) -> None:
        self.redis = RedisRepository()

    async def jwt_save_to_redis(self, jwt_token: str, user_id: int) -> None:
        jwt_token_data = json.dumps(
            {
                "token": jwt_token,
                "expiration_time": (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_TOKEN_EXPIRES)
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "disabled": False,
            }
        )
        await self.redis.add_one(name=user_id, value=jwt_token_data, time=settings.JWT_TOKEN_EXPIRES)


class JWTToken(JWTTokenSaveToRedis):
    async def create_token(self, user_id: int) -> str:
        header = base64.b64encode(str({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(
            str(
                {
                    "user_id": user_id,
                    "expiration_time": (
                        datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_TOKEN_EXPIRES)
                    ).strftime("%Y-%m-%d %H:%M:%S"),
                }
            ).encode()
        ).decode()
        signature = hashlib.sha256((header + payload + settings.JWT_SECRET_KEY).encode()).hexdigest()

        jwt_token = f"{header}.{payload}.{signature}"

        await self.jwt_save_to_redis(jwt_token=jwt_token, user_id=user_id)

        return jwt_token

    @staticmethod
    async def verify_token() -> None:
        # base64.b64decode(payload).decode()
        pass
