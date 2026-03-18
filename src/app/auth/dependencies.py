import uuid
from typing import AsyncIterator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.strategies import CustomJWTStrategy
from app.core.config import settings
from app.database.session import get_async_session
from app.models.user import User


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
) -> AsyncIterator[SQLAlchemyUserDatabase[User, uuid.UUID]]:  # type: ignore[return]
    yield SQLAlchemyUserDatabase(session, User)  # type: ignore[arg-type]


def get_jwt_strategy() -> CustomJWTStrategy:
    return CustomJWTStrategy(
        secret=settings.JWT_SECRET,
        lifetime_seconds=settings.ACCESS_TOKEN_LIFETIME_S,
        token_audience=[
            "api",
        ],
        algorithm="HS256",
    )
