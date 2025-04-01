from sqlalchemy import delete, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.users import DBUser
from src.repositories.base import Repository
from src.schemas.users import UserRepository, User


class DatabaseRepository(Repository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, user_id: int) -> UserRepository | None:
        result = await self.session.execute(select(DBUser).where(DBUser.id == user_id))
        user = result.scalar_one_or_none()
        return UserRepository.model_validate(user) if user else None

    async def create_user(self, user: User) -> UserRepository:
        new_user = DBUser(**user.model_dump())
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return UserRepository.model_validate(new_user)

    async def delete_user(self, user_id: int) -> bool:
        try:
            stmt = delete(DBUser).where(DBUser.id == user_id)
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.rowcount == 1
        except SQLAlchemyError:
            await self.session.rollback()
            return False

    async def update_user(self, user_id: int, user: User) -> bool:
        try:
            stmt = (
                update(DBUser)
                .where(DBUser.id == user_id)
                .values(**user.model_dump())
            )
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.rowcount == 1
        except SQLAlchemyError:
            await self.session.rollback()
            return False