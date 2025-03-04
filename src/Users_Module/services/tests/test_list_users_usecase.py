import pytest
from unittest.mock import AsyncMock, MagicMock
from src.Users_Module.services.list_users_usecase import (
    List_Users_Usecase,
    get_list_users_use_case,
)
from src.Users_Module.repository.User_repository import UserRepository
from src.Users_Module.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_list_users_usecase_execute():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    list_users_usecase = List_Users_Usecase(
        user_repository=mock_user_repository, db=mock_db
    )
    expected_users = [
        User(id="user1", name="User 1", email="user1@example.com", password=b"hashed1"),
        User(id="user2", name="User 2", email="user2@example.com", password=b"hashed2"),
    ]

    mock_user_repository.list_users.return_value = expected_users

    # Act
    result = await list_users_usecase.execute()

    # Assert
    mock_user_repository.list_users.assert_awaited_once_with(mock_db)
    assert result == expected_users


@pytest.mark.asyncio
async def test_get_list_users_usecase():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    mock_get_user_repository = MagicMock(return_value=mock_user_repository)
    mock_get_db = MagicMock(return_value=mock_db)

    # Act
    list_users_usecase = await get_list_users_use_case(
        user_repo=mock_get_user_repository(), db=mock_get_db()
    )

    # Assert
    assert isinstance(list_users_usecase, List_Users_Usecase)
    assert list_users_usecase.user_repository == mock_user_repository
    assert list_users_usecase.db == mock_db
