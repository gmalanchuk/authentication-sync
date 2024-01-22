from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.services.auth import AuthHTTPService
from src.services.email import EmailRabbitMQService


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema,
    auth_service: Annotated[AuthHTTPService, Depends()],
    email_service: Annotated[EmailRabbitMQService, Depends()],
) -> JSONResponse:
    response = await auth_service.registration(request_user)
    await email_service.email_verification_notification(response)
    return response


@auth_router.post(path="/login/", response_model=None)
async def login(
    request_user: UserLoginRequestSchema,
    auth_service: Annotated[AuthHTTPService, Depends()],
) -> JSONResponse:
    return await auth_service.login(request_user)
