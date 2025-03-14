from fastapi import Depends
from database.db import get_db
from src.baseHandlers.Use_Case import Base_Use_Case
from src.Users_Module.repository.User_repository import (
    get_user_repository,
    UserRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession


class SoftDelete_User_Usecase(Base_Use_Case):
    def __init__(self, user_repository: UserRepository, db: AsyncSession):
        self.user_repository = user_repository
        self.db = db

    async def execute(self, id: str, logged_user: str):
        return await self.user_repository.delete_user(
            user_id=id, db=self.db, logged_user=logged_user
        )


async def get_softDelete_user_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> SoftDelete_User_Usecase:
    return SoftDelete_User_Usecase(user_repository=user_repo, db=db)
