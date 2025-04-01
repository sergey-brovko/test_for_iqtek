import pytest
from src.schemas.users import User


@pytest.mark.asyncio
async def test_create_and_get_user(repository):
    user_data = User(full_name="Test")
    created_user = await repository.create_user(user_data)

    fetched_user = await repository.get_user(created_user.id)
    assert fetched_user is not None
    assert fetched_user.full_name == "Test"


@pytest.mark.asyncio(loop_scope="session")
async def test_update_user(repository):
    user_data = User(full_name="Original")
    user = await repository.create_user(user_data)

    update_data = User(full_name="Updated")
    success = await repository.update_user(user.id, update_data)
    assert success is True

    updated_user = await repository.get_user(user.id)
    assert updated_user.full_name == "Updated"


@pytest.mark.asyncio(loop_scope="session")
async def test_delete_user(repository):
    user_data = User(full_name="ToDelete")
    user = await repository.create_user(user_data)

    success = await repository.delete_user(user.id)
    assert success is True

    deleted_user = await repository.get_user(user.id)
    assert deleted_user is None


@pytest.mark.asyncio(loop_scope="session")
async def test_update_non_existing_user(repository):
    success = await repository.update_user(999, User(full_name="test"))
    assert success is False


@pytest.mark.asyncio(loop_scope="session")
async def test_delete_non_existing_user(repository):
    success = await repository.delete_user(999)
    assert success is False