
from fastapi import Depends
from database.db import get_db
from users_api.dtos.create_user_dto import Create_User_DTO
from users_api.models.User_entity import User
from users_api.repository.User_repository import  get_user_repository, UserRepository
from sqlalchemy.ext.asyncio import AsyncSession



class SoftDelete_User_Usecase:
    def __init__(self, user_repository: UserRepository, db: AsyncSession):
        self.user_repository = user_repository
        self.db = db

    async def execute(self, id:str):
        return await self.user_repository.delete_user(id, self.db)


async def get_softDelete_user_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> SoftDelete_User_Usecase:
    return SoftDelete_User_Usecase(user_repository=user_repo, db=db)
