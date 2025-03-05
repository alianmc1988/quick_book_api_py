import pytest
from unittest.mock import AsyncMock, MagicMock
from src.Users_Module.services.get_user_byId_usecase import (
    Get_UserById_Usecase,
    get_userById_use_case,
)
from src.Users_Module.repository.User_repository import UserRepository
from src.Users_Module.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_get_user_by_id_usecase_execute():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    get_user_by_id_usecase = Get_UserById_Usecase(
        user_repository=mock_user_repository, db=mock_db
    )
    user_id = "some_user_id"
    expected_user = User(
        id=user_id,
        name="Test User",
        email="test@example.com",
        password=b"hashed_password",
    )

    mock_user_repository.get_user_by_id.return_value = expected_user

    # Act
    result = await get_user_by_id_usecase.execute(id=user_id)

    # Assert
    mock_user_repository.get_user_by_id.assert_awaited_once_with(
        user_id=user_id, db=mock_db
    )
    assert result == expected_user


@pytest.mark.asyncio
async def test_get_user_by_id_usecase_get_user_by_id_use_case():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    mock_get_user_repository = MagicMock(return_value=mock_user_repository)
    mock_get_db = MagicMock(return_value=mock_db)

    # Act
    get_user_by_id_usecase = await get_userById_use_case(
        user_repo=mock_get_user_repository(), db=mock_get_db()
    )

    # Assert
    assert isinstance(get_user_by_id_usecase, Get_UserById_Usecase)
    assert get_user_by_id_usecase.user_repository == mock_user_repository
    assert get_user_by_id_usecase.db == mock_db
