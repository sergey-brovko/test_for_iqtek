from src.repositories.base import Repository
from src.schemas.users import UserRepository, User


class MemoryRepository(Repository):
    users = dict()
    current_id = 1

    async def get_user(self, user_id: int) -> UserRepository | None:
        if user_id not in MemoryRepository.users:
            return None
        return MemoryRepository.users.get(user_id)

    async def create_user(self, user: User) -> UserRepository:
        user_id = MemoryRepository.current_id
        MemoryRepository.current_id += 1
        new_user = UserRepository(id=user_id, **user.model_dump())
        MemoryRepository.users[user_id] = new_user
        return new_user

    async def delete_user(self, user_id: int) -> bool:
        if user_id not in MemoryRepository.users:
            return False
        MemoryRepository.users.pop(user_id)
        return True

    async def update_user(self, user_id: int, user: User) -> bool:
        if user_id not in MemoryRepository.users:
            return False
        update_user = UserRepository(id=user_id, **user.model_dump())
        MemoryRepository.users[user_id] = update_user
        return True