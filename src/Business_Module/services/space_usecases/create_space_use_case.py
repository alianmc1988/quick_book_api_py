from fastapi import Depends
from database.db import get_db
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.models.business_entity import Business
from src.Business_Module.repository.space_repository import (
    Space_Repository,
    get_space_repository,
)
from src.baseHandlers.Use_Case import Base_Use_Case
from sqlalchemy.ext.asyncio import AsyncSession


class Create_Space_Usecase(Base_Use_Case):
    def __init__(self, space_repository: Space_Repository):
        self.space_repository = space_repository

    async def execute(self, space_payload: Create_Space_DTO) -> Business:
        return await self.space_repository.create_space(space_payload=space_payload)


def get_create_space_usecase(
    space_repository: Space_Repository = Depends(get_space_repository),
) -> Create_Space_Usecase:
    return Create_Space_Usecase(space_repository=space_repository)
