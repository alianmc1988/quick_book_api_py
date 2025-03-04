from fastapi import Depends
from database.db import get_db
from src.Business_Module.repository.business_repository import (
    Business_Repository,
    get_business_repository,
)
from src.Users_Module.value_objects.Role_Type import (
    Staff_Role_literal_Enum,
    conver_literal_to_numeric_role,
    convert_numeric_to_literal_role,
)
from src.baseHandlers.Use_Case import Base_Use_Case
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.models.User_entity import User
from src.Users_Module.repository.User_repository import (
    get_user_repository,
    UserRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession


class Create_User_Usecase(Base_Use_Case):
    def __init__(
        self,
        user_repository: UserRepository,
        business_repository: Business_Repository,
        db: AsyncSession,
    ):
        self.user_repository = user_repository
        self.business_repository = business_repository
        self.db = db

    async def validation_pipe(self, user_id: str, business_id: str):
        user = self.user_repository.get_user_by_id(user_id=user_id, db=self.db)
        business = self.business_repository.get_business_by_id(
            business_id=business_id, db=self.db
        )
        return user

    async def execute(
        self, user_id: str, business_id: str, role: Staff_Role_literal_Enum
    ) -> User:
        role_number = conver_literal_to_numeric_role(role_name=role)
        user = await self.validation_pipe(user_id=user_id, business_id=business_id)
        await self.user_repository.add_role_to_user(
            business_id=business_id, user_id=user_id, role=role_number
        )
        return user


async def get_create_user_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    business_repository: Business_Repository = Depends(get_business_repository),
    db: AsyncSession = Depends(get_db),
) -> Create_User_Usecase:
    return Create_User_Usecase(
        user_repository=user_repo, business_repository=business_repository, db=db
    )
