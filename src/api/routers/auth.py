from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.services.auth import AuthHTTPService
from src.services.email import EmailRabbitMQService


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(request_user: UserRegistrationRequestSchema) -> JSONResponse:
    response = await AuthHTTPService().registration(request_user)
    await EmailRabbitMQService().email_verification_notification(response)
    return response


@auth_router.post(path="/login/", response_model=None)
async def login(request_user: UserLoginRequestSchema) -> JSONResponse:
    return await AuthHTTPService().login(request_user)
