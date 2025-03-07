from fastapi import Depends
from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
from src.Business_Module.models.business_entity import Business
from src.Business_Module.repository.space_repository import (
    Space_Repository,
    get_space_repository,
)
from src.baseHandlers.Use_Case import Base_Use_Case


class Update_Space_Usecase(Base_Use_Case):
    def __init__(self, space_repository: Space_Repository):
        self.space_repository = space_repository

    async def execute(
        self, id: str, space_payload: Create_Space_DTO, logged_user: str
    ) -> Business:
        return await self.space_repository.update_space(
            id=id, space_payload=space_payload, logged_user=logged_user
        )


def get_update_space_usecase(
    space_repository: Space_Repository = Depends(get_space_repository),
) -> Update_Space_Usecase:
    return Update_Space_Usecase(space_repository=space_repository)
