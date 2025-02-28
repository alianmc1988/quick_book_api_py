from typing import List
from fastapi import Depends
from database.db import get_db
from src.Business_Module.repository.business_repository import (
    Business_Repository,
    get_business_repository,
)
from src.Business_Module.models.business_entity import Business
from src.baseHandlers.Use_Case import Base_Use_Case
from sqlalchemy.ext.asyncio import AsyncSession


class List_Businesses_Usecase(Base_Use_Case):
    def __init__(self, business_repository: Business_Repository, db: AsyncSession):
        self.business_repository = business_repository
        self.db = db

    async def execute(self) -> List[Business]:
        return await self.business_repository.list_all_businesses(db=self.db)


def get_list_businesses_usecase(
    business_repository: Business_Repository = Depends(get_business_repository),
    db: AsyncSession = Depends(get_db),
) -> List_Businesses_Usecase:
    return List_Businesses_Usecase(business_repository=business_repository, db=db)
