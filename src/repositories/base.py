from abc import ABC, abstractmethod
from src.schemas import User, UserRepository


class Repository(ABC):
    @abstractmethod
    async def get_user(self, user_id: int) -> UserRepository | None:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> UserRepository:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user: User) -> None:
        pass