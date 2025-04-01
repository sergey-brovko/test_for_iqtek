from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from src.config import settings


engine = create_async_engine(
    f"{settings.database['driver']}://"
    f"{settings.database['user']}:"
    f"{settings.database['password']}@"
    f"{settings.database['host']}:"
    f"{settings.database['port']}/"
    f"{settings.database['name']}"
)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.create_all)
