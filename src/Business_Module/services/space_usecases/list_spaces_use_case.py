from fastapi import Depends
from database.db import get_db
from src.Business_Module.models.business_entity import Business
from src.Business_Module.repository.space_repository import (
    Space_Repository,
    get_space_repository,
)
from src.baseHandlers.Use_Case import Base_Use_Case


class List_Spaces_Usecase(Base_Use_Case):
    def __init__(self, space_repository: Space_Repository):
        self.space_repository = space_repository

    async def execute(self, business_id: str) -> Business:
        return await self.space_repository.list_all_spaces_from_business(
            business_id=business_id
        )


def get_list_spaces_usecase(
    space_repository: Space_Repository = Depends(get_space_repository),
) -> List_Spaces_Usecase:
    return List_Spaces_Usecase(space_repository=space_repository)
