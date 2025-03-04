import pytest
from unittest.mock import AsyncMock, MagicMock
from src.Users_Module.services.softDelete_user_usecase import (
    SoftDelete_User_Usecase,
    get_softDelete_user_use_case,
)
from src.Users_Module.repository.User_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_soft_delete_user_usecase_execute():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    soft_delete_user_usecase = SoftDelete_User_Usecase(
        user_repository=mock_user_repository, db=mock_db
    )
    user_id = "some_user_id"

    # Act
    await soft_delete_user_usecase.execute(id=user_id)

    # Assert
    mock_user_repository.delete_user.assert_awaited_once_with(user_id, mock_db)


@pytest.mark.asyncio
async def test_get_soft_delete_user_usecase():
    # Arrange
    mock_user_repository = AsyncMock(spec=UserRepository)
    mock_db = AsyncMock(spec=AsyncSession)
    mock_get_user_repository = MagicMock(return_value=mock_user_repository)
    mock_get_db = MagicMock(return_value=mock_db)

    # Act
    soft_delete_user_usecase = await get_softDelete_user_use_case(
        user_repo=mock_get_user_repository(), db=mock_get_db()
    )

    # Assert
    assert isinstance(soft_delete_user_usecase, SoftDelete_User_Usecase)
    assert soft_delete_user_usecase.user_repository == mock_user_repository
    assert soft_delete_user_usecase.db == mock_db
