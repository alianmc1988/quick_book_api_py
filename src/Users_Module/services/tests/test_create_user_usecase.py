import pytest
from unittest.mock import AsyncMock, MagicMock
from src.Users_Module.services.create_user_usecase import (
    Create_User_Usecase,
    get_create_user_use_case,
)
from src.Users_Module.repository.User_repository import UserRepository
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_user_usecase_execute():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    create_user_usecase = Create_User_Usecase(
        user_repository=mock_user_repository, db=mock_db
    )
    user_data = Create_User_DTO(
        name="Test User", email="test@example.com", password="password"
    )
    expected_user = User(
        id="some_id",
        name="Test User",
        email="test@example.com",
        password=b"hashed_password",
    )

    mock_user_repository.create_user.return_value = expected_user

    # Act
    result = await create_user_usecase.execute(user=user_data)

    # Assert
    mock_user_repository.create_user.assert_awaited_once_with(user_data, mock_db)
    assert result == expected_user


@pytest.mark.asyncio
async def test_get_create_user_usecase():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    mock_get_user_repository = MagicMock(return_value=mock_user_repository)
    mock_get_db = MagicMock(return_value=mock_db)

    # Act
    create_user_usecase = await get_create_user_use_case(
        user_repo=mock_get_user_repository(), db=mock_get_db()
    )

    # Assert
    assert isinstance(create_user_usecase, Create_User_Usecase)
    assert create_user_usecase.user_repository == mock_user_repository
    assert create_user_usecase.db == mock_db
