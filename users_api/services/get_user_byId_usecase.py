
from fastapi import Depends
from database.db import get_db
from users_api.dtos.update_user_dto import Update_User_DTO
from users_api.models.User_entity import User
from users_api.repository.User_repository import  get_user_repository, UserRepository
from sqlalchemy.ext.asyncio import AsyncSession



class Get_UserById_Usecase:
    def __init__(self, user_repository: UserRepository, db: AsyncSession):
        self.user_repository = user_repository
        self.db = db

    async def execute(self, id: str) -> User:
        return await self.user_repository.get_user_by_id(user_id=id,db=self.db)


async def get_userById_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> Get_UserById_Usecase:
    return Get_UserById_Usecase(user_repository=user_repo, db=db)
