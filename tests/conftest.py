import pytest_asyncio

from src.repositories.memory import MemoryRepository
from src.repositories.database import DatabaseRepository
from src.database.session import async_session, engine
from src.models.users import DBUser


@pytest_asyncio.fixture(params=["memory", "sql"])
async def repo_type(request):
    return request.param


@pytest_asyncio.fixture
async def repository(repo_type):
    if repo_type == "memory":
        yield MemoryRepository()

    async with engine.begin() as conn:
        await conn.run_sync(DBUser.metadata.create_all)

    if repo_type == "sql":
        async with async_session() as session:
            yield DatabaseRepository(session)

    async with engine.begin() as conn:
        await conn.run_sync(DBUser.metadata.drop_all)