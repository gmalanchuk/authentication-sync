import base64
import hashlib

from starlette.responses import JSONResponse

from src.config import settings


class JWTToken:
    @staticmethod
    async def create_token(user_obj: dict, response: JSONResponse) -> None:
        header = base64.b64encode(str({"alg": "HS256", "typ": "JWT"}).encode()).decode()
        payload = base64.b64encode(str({"user_id": user_obj["id"]}).encode()).decode()
        signature = hashlib.sha256((header + payload + settings.JWT_SECRET_KEY).encode()).hexdigest()

        jwt_token = f"{header}.{payload}.{signature}"

        response.set_cookie(key="access_token", value=jwt_token, expires=settings.JWT_TOKEN_EXPIRES)

    @staticmethod
    async def verify_token() -> None:
        # base64.b64decode(payload).decode()
        pass
