from fastapi import Depends
from database.db import get_db
from src.Business_Module.dtos.business_dtos.update_business_dto import (
    Update_Business_DTO,
)
from src.Business_Module.repository.business_repository import (
    Business_Repository,
    get_business_repository,
)
from src.Business_Module.models.business_entity import Business
from src.baseHandlers.Use_Case import Base_Use_Case
from sqlalchemy.ext.asyncio import AsyncSession


class Update_Business_Usecase(Base_Use_Case):
    def __init__(self, business_repository: Business_Repository, db: AsyncSession):
        self.business_repository = business_repository
        self.db = db

    async def execute(
        self, business_id: str, business_payload: Update_Business_DTO, logged_user: str
    ) -> Business:
        return await self.business_repository.update_business(
            business_id=business_id,
            business_payload=business_payload,
            db=self.db,
            logged_user=logged_user,
        )


def update_business_usecase(
    business_repository: Business_Repository = Depends(get_business_repository),
    db: AsyncSession = Depends(get_db),
) -> Update_Business_Usecase:
    return Update_Business_Usecase(business_repository=business_repository, db=db)
