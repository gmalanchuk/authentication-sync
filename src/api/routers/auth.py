from fastapi import APIRouter, Depends
from sqlalchemy import select

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.database.models import User
from src.database.session import async_session
from src.services.auth import AuthService
from src.services.dependencies import get_auth_service
from src.utils.hash_password import HashPassword


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema, auth_service: AuthService = Depends(get_auth_service)
) -> UserRegistrationResponseSchema:
    return await auth_service.registration(request_user)


@auth_router.post(path="/login/")
async def login(request_user: UserLoginRequestSchema) -> bool | None:
    hash_password = HashPassword()

    user_dict = request_user.model_dump()

    async with async_session() as session:
        q = select(User).where(User.email == user_dict["email"])
        user_exist = (await session.execute(q)).scalars().first()
        if user_exist:
            res = hash_password.verify_hash(user_dict["password"], user_exist.hashed_password)
            return res

        return None
