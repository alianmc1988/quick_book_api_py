import pytest
from unittest.mock import AsyncMock
from src.Business_Module.services.busines_usecases.create_business_use_case import (
    get_create_business_usecase,
)
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.models.business_entity import Business
from src.Business_Module.value_objects.Business_Type import Business_Type_Enum
from src.Business_Module.repository.business_repository import Business_Repository
from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

fake = Faker()


@pytest.mark.asyncio
async def test_create_business_usecase_execute():
    # Arrange
    # Dependencies
    mock_business_repository = AsyncMock(spec=Business_Repository)
    mock_db = AsyncMock(spec=AsyncSession)

    # Usecase
    create_business_usecase = get_create_business_usecase(
        business_repository=mock_business_repository, db=mock_db
    )

    address = fake.address()
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    other_phone = fake.phone_number()
    type_bar = Business_Type_Enum.BAR

    # Payload
    business_payload = Create_Business_DTO(
        address=address,
        name=name,
        email=email,
        phone=phone,
        other_phone=other_phone,
        type=type_bar,
    )

    # Expected Result
    expected_business = Business(
        name=name,
        address=address,
        email=email,
        phone=phone,
        other_phone=other_phone,
        type=type_bar,  # add type to expected result
    )

    mock_business_repository.create_business.return_value = expected_business

    # Act
    result = await create_business_usecase.execute(business_payload=business_payload)

    # Assert
    mock_business_repository.create_business.assert_awaited_once_with(
        business_payload=business_payload, db=mock_db
    )
    assert result == expected_business
