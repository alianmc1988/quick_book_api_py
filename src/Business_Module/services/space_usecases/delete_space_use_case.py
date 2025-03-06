from fastapi import Depends
from src.Business_Module.repository.space_repository import (
    Space_Repository,
    get_space_repository,
)
from src.baseHandlers.Use_Case import Base_Use_Case


class Delete_Space_Usecase(Base_Use_Case):
    def __init__(self, space_repository: Space_Repository):
        self.space_repository = space_repository

    async def execute(self, id: str, logged_user: str) -> None:
        return await self.space_repository.delete_space(id=id)


def get_delete_space_usecase(
    space_repository: Space_Repository = Depends(get_space_repository),
) -> Delete_Space_Usecase:
    return Delete_Space_Usecase(space_repository=space_repository)
