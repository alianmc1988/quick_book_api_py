from fastapi import Depends
from database.db import get_db
from src.baseHandlers.Use_Case import Base_Use_Case
from src.Users_Module.dtos.update_user_dto import Update_User_DTO
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import (
    get_user_repository,
    UserRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession


class Update_User_Usecase(Base_Use_Case):
    def __init__(self, user_repository: UserRepository, db: AsyncSession):
        self.user_repository = user_repository
        self.db = db

    async def execute(self, id: str, user: Update_User_DTO) -> User:
        return await self.user_repository.update_user(
            user_id=id, user_data=user, db=self.db
        )


async def get_update_user_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> Update_User_Usecase:
    return Update_User_Usecase(user_repository=user_repo, db=db)
