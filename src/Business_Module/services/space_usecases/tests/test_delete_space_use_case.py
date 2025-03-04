import pytest
from unittest.mock import AsyncMock, MagicMock
from src.Business_Module.services.space_usecases.delete_space_use_case import (
    Delete_Space_Usecase,
    get_delete_space_usecase,
)
from src.Business_Module.repository.space_repository import Space_Repository


@pytest.mark.asyncio
async def test_delete_space_usecase_execute():
    # Arrange
    mock_space_repository = AsyncMock(spec=Space_Repository)
    delete_space_usecase = Delete_Space_Usecase(space_repository=mock_space_repository)
    space_id = "some_space_id"

    # Act
    await delete_space_usecase.execute(id=space_id)

    # Assert
    mock_space_repository.delete_space.assert_awaited_once_with(id=space_id)


@pytest.mark.asyncio
async def test_get_delete_space_usecase():
    # Arrange
    mock_space_repository = AsyncMock(spec=Space_Repository)
    mock_get_space_repository = MagicMock(return_value=mock_space_repository)

    # Act
    delete_space_usecase = get_delete_space_usecase(
        space_repository=mock_get_space_repository()
    )

    # Assert
    assert isinstance(delete_space_usecase, Delete_Space_Usecase)
    assert delete_space_usecase.space_repository == mock_space_repository
