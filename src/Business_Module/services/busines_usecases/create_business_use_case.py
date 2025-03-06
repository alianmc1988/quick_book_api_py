from typing import List
from fastapi import Depends
from database.db import get_db
from src.Business_Module.dtos.business_dtos.create_business_dto import (
    Create_Business_DTO,
)
from src.Business_Module.repository.business_repository import (
    Business_Repository,
    get_business_repository,
)
from src.Business_Module.models.business_entity import Business
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import (
    UserRepository,
    get_user_repository,
)
from src.baseHandlers.Use_Case import Base_Use_Case
from sqlalchemy.ext.asyncio import AsyncSession


class Create_Business_Usecase(Base_Use_Case):
    def __init__(
        self,
        business_repository: Business_Repository,
        db: AsyncSession,
        user_repository: UserRepository,
    ):
        self.business_repository = business_repository
        self.user_repository = user_repository
        self.db = db

    async def execute(self, business_payload: Create_Business_DTO) -> Business:
        master_users: List[User] = await self.user_repository.find_master_users(
            db=self.db
        )
        return await self.business_repository.create_business(
            business_payload=business_payload, db=self.db, master_users=master_users
        )


def get_create_business_usecase(
    business_repository: Business_Repository = Depends(get_business_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> Create_Business_Usecase:
    return Create_Business_Usecase(
        business_repository=business_repository, db=db, user_repository=user_repository
    )
