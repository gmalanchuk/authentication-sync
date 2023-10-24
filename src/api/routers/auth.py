from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.database.models import User
from src.database.session import get_async_session


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema, session: AsyncSession = Depends(get_async_session)
) -> UserRegistrationResponseSchema:
    stmt = insert(User).values(**request_user.model_dump()).returning(User.__table__)
    res = await session.execute(stmt)
    await session.commit()
    return UserRegistrationResponseSchema(**dict(res.fetchone()._mapping))
