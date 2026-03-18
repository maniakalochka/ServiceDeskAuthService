from typing import AsyncIterator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.app.core.config import settings

DATABASE_URL = settings.POSTGRES_AUTH_URL
DATABASE_PARAMS = {
    "poolclass": NullPool,
}

engine = create_async_engine(url=DATABASE_URL, echo=False, **DATABASE_PARAMS)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
