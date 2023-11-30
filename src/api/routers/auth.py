from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.services.auth import AuthService
from src.services.dependencies import get_auth_service


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema, auth_service: AuthService = Depends(get_auth_service)
) -> JSONResponse:
    return await auth_service.registration(request_user)


@auth_router.post(path="/login/", response_model=None)
async def login(
    request_user: UserLoginRequestSchema, auth_service: AuthService = Depends(get_auth_service)
) -> JSONResponse | None:
    return await auth_service.login(request_user)
