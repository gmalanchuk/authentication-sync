import ast
import base64
import datetime
import hashlib
import json

from src.config import settings
from src.repositories.base.redis import RedisRepository
from src.services.enums.tag import TagEnum
from src.services.exceptions.grpc_exceptions import GRPCExceptions
from src.services.exceptions.http_exceptions import HTTPExceptions


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
    def __init__(self, tag: TagEnum) -> None:
        super().__init__()
        self.http_exception = HTTPExceptions()
        self.grpc_exception = GRPCExceptions()
        self.tag = tag

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
    async def verify_token(header: str, payload: str, signature: str) -> bool:
        header_payload_hash = hashlib.sha256((header + payload + settings.JWT_SECRET_KEY).encode()).hexdigest()
        if header_payload_hash == signature:
            return True

        return False

    async def decode_token(self, token: str) -> dict:
        header, payload, signature = token.split(".")
        if not await self.verify_token(header, payload, signature):
            if self.tag == TagEnum.HTTP:
                return await self.http_exception.is_invalid(value1="JWT token")
            elif self.tag == TagEnum.GRPC:
                return await self.grpc_exception.is_invalid(value1="JWT token")
        decoded_payload = ast.literal_eval(base64.b64decode(payload).decode())

        value = await self.redis.get_one(name=decoded_payload["user_id"])

        if not value:
            if self.tag == TagEnum.HTTP:
                return await self.http_exception.has_expired(value="JWT token")
            elif self.tag == TagEnum.GRPC:
                return await self.grpc_exception.has_expired(value="JWT token")

        return decoded_payload
