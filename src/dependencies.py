from fastapi import Request
from src.config import settings
from src.database import async_session
from src.repositories.database import DatabaseRepository
from src.repositories.memory import MemoryRepository


async def get_repository(request: Request):
    if settings.repository_type == "memory":
        yield MemoryRepository()
    elif settings.repository_type == "sql":
        async with async_session() as session:
            yield DatabaseRepository(session)