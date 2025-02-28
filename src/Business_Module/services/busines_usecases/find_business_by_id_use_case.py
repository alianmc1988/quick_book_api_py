from fastapi import Depends
from database.db import get_db
from src.Business_Module.repository.business_repository import Business_Repository, get_business_repository
from src.Business_Module.models.business_entity import Business
from src.baseHandlers.Use_Case import Base_Use_Case
from sqlalchemy.ext.asyncio import AsyncSession


class Find_Business_By_Id_Usecase(Base_Use_Case):
    def __init__(self, business_repository: Business_Repository, db:AsyncSession):
        self.business_repository = business_repository
        self.db = db

    async def execute(self, business_id:str)-> Business:
        return await self.business_repository.get_business_by_id(business_id=business_id,db=self.db)
    
def find_business_by_id_usecase(
       business_repository: Business_Repository = Depends(get_business_repository),
       db: AsyncSession = Depends(get_db)
)->Find_Business_By_Id_Usecase:
    return Find_Business_By_Id_Usecase(business_repository=business_repository, db=db)