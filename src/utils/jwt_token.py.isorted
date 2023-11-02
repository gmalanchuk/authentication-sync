import base64
import hashlib

from src.config import settings


class JWTToken:
    @staticmethod
    async def create_token(user_id: dict) -> str:
        header = base64.b64encode(str({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(str({"user_id": user_id}).encode()).decode()
        signature = hashlib.sha256((header + payload + settings.JWT_SECRET_KEY).encode()).hexdigest()

        jwt_token = f"{header}.{payload}.{signature}"

        return jwt_token

    @staticmethod
    async def verify_token() -> None:
        # base64.b64decode(payload).decode()
        pass
