from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

engine = create_async_engine(settings.database_url)
async_session = async_sessionmaker(engine, expire_on_commit=False, autoflush=False, autocommit=False)


@asynccontextmanager
async def get_session():
    async with async_session() as session:
        yield session
