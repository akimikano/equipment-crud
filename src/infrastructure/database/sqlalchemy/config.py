from typing import AsyncGenerator, TypeAlias, Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    url="postgresql+asyncpg://demo:demo@localhost:5432/equipmentdb",
    echo=True
)


async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_db_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


DbSession: TypeAlias = Annotated[AsyncSession, Depends(get_db_session)]
