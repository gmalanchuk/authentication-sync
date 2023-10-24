from fastapi import APIRouter

from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.services.auth import AuthService


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(request_user: UserRegistrationRequestSchema) -> UserRegistrationResponseSchema:
    return await AuthService().registration(request_user)
